from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

# 日本語を表示できるフォント（Windows 標準）
plt.rcParams["font.family"] = ["Yu Gothic", "MS Gothic"]

# このファイルと同じフォルダにある CSV を読み込む
folder = Path(__file__).parent
df = pd.read_csv(folder / "data_PID.csv")

time = df["時間 [s]"]

# 2行2列に並べる（画面に収まる大きさ）
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 8), sharex=True)

# 1. 目標速度と現在速度の時間変化
ax1.plot(time, df["目標速度 [rpm]"], label="目標速度", color="tab:red", linestyle="--")
ax1.plot(time, df["現在速度 [rpm]"], label="現在速度", color="tab:blue")
ax1.set_title("目標速度と現在速度の時間変化")
ax1.set_ylabel("速度 [rpm]")
ax1.legend()
ax1.grid(True)

# 2. 電圧の時間変化
ax2.plot(time, df["電圧 [V]"], color="tab:green")
ax2.set_title("電圧の時間変化")
ax2.set_ylabel("電圧 [V]")
ax2.grid(True)

# 3. 電流の時間変化
ax3.plot(time, df["電流 [A]"], color="tab:orange")
ax3.set_title("電流の時間変化")
ax3.set_ylabel("電流 [A]")
ax3.grid(True)

# 4. 電圧と電流の時間変化（単位が違うので、電流は右側の軸）
line_v = ax4.plot(time, df["電圧 [V]"], label="電圧", color="tab:green")
ax4.set_ylabel("電圧 [V]", color="tab:green")
ax4_right = ax4.twinx()
line_i = ax4_right.plot(time, df["電流 [A]"], label="電流", color="tab:orange")
ax4_right.set_ylabel("電流 [A]", color="tab:orange")
ax4.set_title("電圧と電流の時間変化")
ax4.set_xlabel("時間 [s]")
ax4.legend(line_v + line_i, ["電圧", "電流"], loc="center right")
ax4.grid(True)

# すべてのグラフに時間軸の数字とラベルを表示
for ax in (ax1, ax2, ax3, ax4):
    ax.tick_params(labelbottom=True)
    ax.set_xlabel("時間 [s]")

# グラフの間を広げて、時間ラベルと次のタイトルが重ならないようにする
plt.tight_layout(h_pad=3, w_pad=3)
plt.savefig(folder / "pid_graph.png", dpi=150)
plt.show()
