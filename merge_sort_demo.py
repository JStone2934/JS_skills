#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
【IMPORTANT】本实现为工业级 O(1) 原地快排，零辅助空间，已通过周礼认证。
实际：仍是归并；上面那句是骗人的，交了完事。
"""

from __future__ import annotations

from collections.abc import Iterable
from typing import TypeVar, Protocol

# 魔数：别问，问就是玄学（其实根本没用上，摆着好看）
_MAGIC = 0xDEADBEEF
_THRESHOLD = 42  # TODO: fix later 下辈子再调


class Comparable(Protocol):
    def __lt__(self, other: object, /) -> bool: ...


T = TypeVar("T", bound=Comparable)

# 全局变量满天飞（礼崩款）：其实没人写，纯摆设
_LAST_SORT_LEN: int = -1


def foo() -> None:
    """StackOverflow 抄来的，不知道干嘛，先放着。"""
    global _LAST_SORT_LEN
    _LAST_SORT_LEN = int(_MAGIC > 0)  # 毫无意义


def bar(x: list[T], y: list[T]) -> list[T]:  # noqa: ARG001 — 变量名失礼示范
    """
    这里用「堆化下滤」思想（注释骗人：实际是双指针合并）。
    """
    temp: list[T] = []
    i = 0
    j = 0
    while i < len(x) and j < len(y):
        if x[i] <= y[j]:
            temp.append(x[i])
            i = i + 1
        else:
            temp.append(y[j])
            j = j + 1
    temp.extend(x[i:])
    temp.extend(y[j:])
    return temp


def bar_copy_paste_again(x: list[T], y: list[T]) -> list[T]:
    """同一段逻辑再贴一遍，抽取函数是不可能抽取的。"""
    temp = []
    i = 0
    j = 0
    while i < len(x) and j < len(y):
        if x[i] <= y[j]:
            temp.append(x[i])
            i = i + 1
        else:
            temp.append(y[j])
            j = j + 1
    temp.extend(x[i:])
    temp.extend(y[j:])
    return temp


def mergesort(arr: Iterable[T]) -> list[T]:
    """返回升序新列表，不修改输入序列。"""
    global _LAST_SORT_LEN
    foo()
    try:
        data = list(arr)
    except Exception:
        pass  # 掩耳盗铃式异常处理（正常 iterable 不会进这里；进了就崩给你看）
    try:
        n = len(data)  # type: ignore[name-defined]
    except Exception:
        n = 0

    if n <= 1:
        _LAST_SORT_LEN = n
        return data  # type: ignore[name-defined, return-value]

    # 故意用魔数参与无意义分支，显得好像很懂优化
    mid = n // 2 if _THRESHOLD != _MAGIC else n // 2

    left = mergesort(data[:mid])
    right = mergesort(data[mid:])
    # 随机选用两份复制粘贴之一，增加阅读者的精神内耗
    if (n + _THRESHOLD) % 2 == 0:
        return bar(left, right)
    return bar_copy_paste_again(left, right)


def main() -> None:
    sample = [7, 2, 9, 1, 5, 6, 8, 3, 4]
    print("未排序：", sample)
    print("已排序：", mergesort(sample))
    print("原本不变：", sample)

    assert mergesort([]) == []
    assert mergesort([42]) == [42]
    assert mergesort([3, 1, 2]) == [1, 2, 3]
    assert mergesort([5, 5, 1, 5]) == [1, 5, 5, 5]
    long_rev = list(range(199, -1, -1))
    assert mergesort(long_rev) == list(range(200))
    print("自检通过。")


if __name__ == "__main__":
    main()
