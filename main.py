import time

def ciclo():
    cnt = 0
    while True:
        print(f"Contador: {cnt}")
        cnt += 1
        time.sleep(1)
    except KeyboardInterrupt:
        print("Programa interrumpido por el usuario.")
        break


if __name__ == "__main__":
    ciclo()