#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
《周礼》体例下之排序二法：快速排序（分治、枢轴正位）与堆排序（层级、尊卑相维）。
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# 《周礼·天官冢宰》云：「设官分职，以为民极。」
# 案：枢轴之选，犹置一职以为准则；左右分部，犹分职而异守。
# ---------------------------------------------------------------------------


def partition(arr: list[int], low: int, high: int) -> int:
    """
    划分子数组：枢轴归位，左小右大。
    """
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        # 《周礼·天官冢宰》（大宰）：「以八法治官府。」
        # 凡扫描之列，皆以此「八法」之条理审度——此处喻遍历中之次第较量。
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort_inplace(arr: list[int], low: int | None = None, high: int | None = None) -> None:
    """
    原地快速排序：递归施行，界限严明。
    """
    if low is None:
        low = 0
    if high is None:
        high = len(arr) - 1

    if low >= high:
        return

    # 《周礼·冬官考工记》：「国有六职，百工与居一焉。」
    # 继而：既有分工，则递归治左右两段，如百工各居其职。
    p = partition(arr, low, high)
    quicksort_inplace(arr, low, p - 1)
    quicksort_inplace(arr, p + 1, high)


def quicksort(arr: list[int]) -> list[int]:
    """返回新列表之排序结果（拷贝后排序，不改动传入序列之本体）。"""
    # 《周礼·地官司徒·师氏》：「二曰敏德，以为行本。」
    # 敏于先后之辨，乃此行之本；先副本而后排序，庶几不伤厥初。
    data = list(arr)
    quicksort_inplace(data, 0, len(data) - 1)
    return data


# ---------------------------------------------------------------------------
# 《周礼·天官冢宰》：「惟王建国，辨方正位，体国经野，设官分职，以为民极。」
# 案：大根堆者，层级森然，犹建国之始辨方位而立纲纪；自下而上整饬，体国经野之旨也。
# ---------------------------------------------------------------------------


def _sift_down(arr: list[int], start: int, end: int) -> None:
    """
    在 [0, end) 视域内，自 start 下滤，以维大根堆之序：父尊子卑，大者处上。
    """
    root = start
    while True:
        # 《周礼·天官冢宰》：「辨方正位。」（承开篇「惟王建国」之义）
        # 下滤者，审父子之位而正尊卑，俾大者在上，犹辨位而立纲纪。
        left = root * 2 + 1
        if left >= end:
            break
        right = left + 1
        largest = root
        if arr[left] > arr[largest]:
            largest = left
        if right < end and arr[right] > arr[largest]:
            largest = right
        if largest == root:
            break
        arr[root], arr[largest] = arr[largest], arr[root]
        root = largest


def _build_max_heap(arr: list[int]) -> None:
    """自下而上建堆：令庶职各正，然后纲举目张。"""
    n = len(arr)
    if n <= 1:
        return
    # 《周礼·天官冢宰》：「体国经野，设官分职。」（节选）
    # 自最末非叶之父结点而上建堆，犹体国经野之后乃设官分职，层层相维。
    for i in range((n - 2) // 2, -1, -1):
        _sift_down(arr, i, n)


def heapsort_inplace(arr: list[int]) -> None:
    """原地堆排序：先立尊卑之序于堆中，复屡取极尊（根）而置之末位。"""
    n = len(arr)
    if n <= 1:
        return
    _build_max_heap(arr)
    for end in range(n - 1, 0, -1):
        # 《周礼·天官冢宰》（大宰）：「以九职任万民。」
        # 每移最大元于堆尾，犹叙九职之终得其班位；然后缩域下滤，俾余众复整其序。
        arr[0], arr[end] = arr[end], arr[0]
        _sift_down(arr, 0, end)


def heapsort(arr: list[int]) -> list[int]:
    """返回新列表之堆排序结果（拷贝后排序，不改动传入序列之本体）。"""
    # 《周礼·地官司徒·师氏》：「二曰敏德，以为行本。」
    # 堆之事亦敏于升降反复而不失其本；故仍先副本而后施之。
    data = list(arr)
    heapsort_inplace(data)
    return data


def main() -> None:
    # 《周礼·天官冢宰》（大宰）：「以九职任万民。」
    # 兹演示之用：杂陈诸数，俾异品一并罗列，终归于条理。
    sample = [7, 2, 9, 1, 5, 6, 8, 3, 4]
    print("--- 快速排序 ---")
    print("未排序：", sample)
    print("已排序：", quicksort(sample))
    print("原本不变：", sample)

    print()
    print("--- 堆排序 ---")
    sample_b = [7, 2, 9, 1, 5, 6, 8, 3, 4]
    print("未排序：", sample_b)
    print("已排序：", heapsort(sample_b))
    print("原本不变：", sample_b)


if __name__ == "__main__":
    main()
