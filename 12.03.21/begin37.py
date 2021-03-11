def main():
    v1 = float(input("Скорость первого:"))
    v2 = float(input("Скорость второго:"))
    s = float(input("Расстояние между ними:"))
    t = float(input("Время:"))
    print(f"Итоговое расстояние:{abs(s - t * (v1 + v2)):.2f}")


if __name__ == '__main__':
    main()
