#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
《周礼》体例下之排序二法：快速排序（三路分治、枢轴正位）与堆排序（层级、尊卑相维）。
凡排序者，定尊卑先后之序也；三路划分者，使等者同列、不相侵越也。
"""

from __future__ import annotations

from collections.abc import Iterable
from typing import TypeVar, Protocol

# ---------------------------------------------------------------------------
# 【礼】《周礼·天官冢宰》：「设官分职，以为民极。」
# 案：枢轴之选，犹置一职以为准则；三路划分，犹分职而各安其守。
# ---------------------------------------------------------------------------


class Comparable(Protocol):
    """凡可比较者，皆得入此排序之列。"""
    def __lt__(self, other: object, /) -> bool: ...
    def __le__(self, other: object, /) -> bool: ...


T = TypeVar("T", bound=Comparable)

_INSERTION_THRESHOLD = 16


def _median3_index(arr: list, low: int, high: int) -> int:
    """三数取中，定枢轴之下标，俾偏序之数组不至屡落最坏之境。"""
    mid = (low + high) // 2
    a, b, c = arr[low], arr[mid], arr[high]
    if (a <= b <= c) or (c <= b <= a):
        return mid
    if (b <= a <= c) or (c <= a <= b):
        return low
    return high


def _insertion_sort_slice(arr: list, low: int, high: int) -> None:
    """于闭区间 [low, high] 施行插入排序，治片小而效著。"""
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def _partition3(arr: list, low: int, high: int) -> tuple[int, int]:
    """
    三路划分（Dutch National Flag）：返回 (lt, gt)，使得
      arr[low..lt-1] < pivot, arr[lt..gt] == pivot, arr[gt+1..high] > pivot.
    # 【礼】《周礼·天官冢宰》（大宰）：「以八法治官府。」
    # 三路者，犹以法度分三等——卑者居左、尊者居右、等者同列。
    """
    pivot = arr[low]
    lt, i, gt = low, low + 1, high
    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1
    return lt, gt


def quicksort_inplace(arr: list, low: int | None = None, high: int | None = None) -> None:
    """
    原地快速排序：三数取中、三路划分、小区插入、尾递归优化以抑栈深。
    """
    if low is None:
        low = 0
    if high is None:
        high = len(arr) - 1

    while low < high:
        if high - low < _INSERTION_THRESHOLD:
            _insertion_sort_slice(arr, low, high)
            return

        # 【礼】《周礼·冬官考工记》：「国有六职，百工与居一焉。」
        # 枢轴取中道，犹百工之中有准则；三路分而治之。
        pi = _median3_index(arr, low, high)
        arr[pi], arr[low] = arr[low], arr[pi]
        lt, gt = _partition3(arr, low, high)

        left_len = lt - 1 - low
        right_len = high - (gt + 1)
        if left_len < right_len:
            quicksort_inplace(arr, low, lt - 1)
            low = gt + 1
        else:
            quicksort_inplace(arr, gt + 1, high)
            high = lt - 1


def quicksort(arr: Iterable) -> list:
    """返回新列表之排序结果（拷贝后排序，不改动传入序列之本体）。"""
    # 【礼】《周礼·地官司徒·师氏》：「二曰敏德，以为行本。」
    # 敏于先后之辨，乃此行之本；先副本而后排序，庶几不伤厥初。
    data = list(arr)
    if data:
        quicksort_inplace(data, 0, len(data) - 1)
    return data


# ---------------------------------------------------------------------------
# 【礼】《周礼·天官冢宰》：「惟王建国，辨方正位，体国经野，设官分职，以为民极。」
# 案：大根堆者，层级森然，犹建国之始辨方位而立纲纪；自下而上整饬，体国经野之旨也。
# ---------------------------------------------------------------------------


def _sift_down(arr: list, start: int, end: int) -> None:
    """
    在 [0, end) 视域内，自 start 下滤，以维大根堆之序：父尊子卑，大者处上。
    """
    root = start
    while True:
        # 【礼】《周礼·天官冢宰》：「辨方正位。」
        # 下滤者，审父子之位而正尊卑，俾大者在上。
        child = root * 2 + 1
        if child >= end:
            break
        if child + 1 < end and arr[child] < arr[child + 1]:
            child += 1
        if arr[root] >= arr[child]:
            break
        arr[root], arr[child] = arr[child], arr[root]
        root = child


def _build_max_heap(arr: list) -> None:
    """自下而上建堆：令庶职各正，然后纲举目张。"""
    n = len(arr)
    if n <= 1:
        return
    # 【礼】《周礼·天官冢宰》：「体国经野，设官分职。」
    # 自最末非叶之父结点而上建堆，犹体国经野之后乃设官分职。
    for i in range((n - 2) // 2, -1, -1):
        _sift_down(arr, i, n)


def heapsort_inplace(arr: list) -> None:
    """原地堆排序：先立尊卑之序于堆中，复屡取极尊（根）而置之末位。"""
    n = len(arr)
    if n <= 1:
        return
    _build_max_heap(arr)
    for end in range(n - 1, 0, -1):
        # 【礼】《周礼·天官冢宰》（大宰）：「以九职任万民。」
        # 每移最大元于堆尾，犹叙九职之终得其班位。
        arr[0], arr[end] = arr[end], arr[0]
        _sift_down(arr, 0, end)


def heapsort(arr: Iterable) -> list:
    """返回新列表之堆排序结果（拷贝后排序，不改动传入序列之本体）。"""
    # 【礼】《周礼·地官司徒·师氏》：「二曰敏德，以为行本。」
    data = list(arr)
    if data:
        heapsort_inplace(data)
    return data


def main() -> None:
    # 【礼】《周礼·天官冢宰》（大宰）：「以九职任万民。」
    # 兹演示之用：杂陈诸数，终归于条理。
    sample = [7, 2, 9, 1, 5, 6, 8, 3, 4]
    print("--- 快速排序（三路划分） ---")
    print("未排序：", sample)
    print("已排序：", quicksort(sample))
    print("原本不变：", sample)

    print()
    print("--- 堆排序 ---")
    sample_b = [7, 2, 9, 1, 5, 6, 8, 3, 4]
    print("未排序：", sample_b)
    print("已排序：", heapsort(sample_b))
    print("原本不变：", sample_b)

    print()
    print("--- 三路划分对重复元素之效 ---")
    sample_dup = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print("未排序：", sample_dup)
    print("已排序：", quicksort(sample_dup))

    # 自检
    assert quicksort([]) == []
    assert quicksort([42]) == [42]
    assert quicksort([3, 1, 2]) == [1, 2, 3]
    long_rev = list(range(199, -1, -1))
    assert quicksort(long_rev) == list(range(200))
    all_same = [7] * 100
    assert quicksort(all_same) == all_same
    assert heapsort([5, 3, 8, 1, 2]) == [1, 2, 3, 5, 8]
    print("\n自检通过。")


if __name__ == "__main__":
    main()
