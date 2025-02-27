import tkinter as tk
from tkinter import ttk, filedialog, colorchooser, messagebox
from PIL import Image, ImageDraw, ImageFont, ImageTk
import os

# 现代风格配色方案
COLOR_SCHEME = {
    "background": "#DCDCDC",
    "foreground": "#000000",
    "accent": "#3498DB",
    "secondary": "#E6E6FA",
    "hover": "#5DADE2"
}


class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("图片水印添加工具")
        self.root.configure(bg=COLOR_SCHEME["background"])

        # 设置窗口初始大小
        self.root.geometry("1200x800")
        self.root.minsize(1000, 700)

        # 初始化变量
        self.image_path = None
        self.original_image = None
        self.display_image = None
        self.watermark_text = tk.StringVar()
        self.angle = tk.IntVar(value=0)
        self.size = tk.IntVar(value=30)
        self.opacity = tk.IntVar(value=128)
        self.watermark_color = (255, 255, 255)  # 默认水印颜色为白色
        self.horizontal_spacing = tk.IntVar(value=150)
        self.vertical_spacing = tk.IntVar(value=100)

        # 创建样式对象
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self._configure_styles()

        # 创建界面组件
        self.create_widgets()

    def _configure_styles(self):
        """配置自定义样式"""
        self.style.configure(
            "TFrame",
            background=COLOR_SCHEME["background"]
        )

        self.style.configure(
            "TLabel",
            background=COLOR_SCHEME["background"],
            foreground=COLOR_SCHEME["foreground"],
            font=("微软雅黑", 10)
        )

        self.style.configure(
            "TButton",
            background=COLOR_SCHEME["accent"],
            foreground=COLOR_SCHEME["foreground"],
            font=("微软雅黑", 10, "bold"),
            borderwidth=0
        )

        self.style.map("TButton",
                       background=[("active", COLOR_SCHEME["hover"])])

        self.style.configure(
            "TScale",
            background=COLOR_SCHEME["background"],
            troughcolor=COLOR_SCHEME["secondary"],
            sliderrelief="flat"
        )

        self.style.configure(
            "TEntry",
            fieldbackground="#404040",
            foreground=COLOR_SCHEME["foreground"],
            insertcolor=COLOR_SCHEME["foreground"]
        )
        # 修改输入框背景颜色
        self.style.configure(
            "TEntry",
            fieldbackground="#FFFAFA",  # 修改为你想要的背景颜色
            foreground=COLOR_SCHEME["foreground"],
            insertcolor=COLOR_SCHEME["foreground"]
        )

    def create_widgets(self):
        # 创建主容器
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # 左侧控制面板
        control_frame = ttk.Frame(main_frame, width=300)
        control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        # 右侧图片显示区域
        self.image_frame = ttk.Frame(main_frame)
        self.image_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # 控制面板内容
        self._build_control_panel(control_frame)

        # 图片显示区域
        self._build_image_display()

    def _build_control_panel(self, parent):
        """构建左侧控制面板"""
        # 导入/导出区域
        io_frame = ttk.LabelFrame(parent, text="文件操作", padding=10)
        io_frame.pack(fill=tk.X, pady=5)

        ttk.Button(io_frame, text="导入图片", command=self.import_image).pack(fill=tk.X, pady=2)
        ttk.Button(io_frame, text="导出图片", command=self.export_image).pack(fill=tk.X, pady=2)

        # 文本设置区域
        text_frame = ttk.LabelFrame(parent, text="水印内容", padding=10)
        text_frame.pack(fill=tk.X, pady=5)

        self.text_entry = ttk.Entry(text_frame, textvariable=self.watermark_text)
        self.text_entry.pack(fill=tk.X, pady=5)
        self.text_entry.insert(0, "请输入水印内容")

        ttk.Button(text_frame, text="选择颜色", command=self.choose_color).pack(fill=tk.X, pady=5)

        # 样式设置区域
        style_frame = ttk.LabelFrame(parent, text="样式设置", padding=10)
        style_frame.pack(fill=tk.X, pady=5)

        self._create_scale(style_frame, "方向", self.angle, 0, 360)
        self._create_scale(style_frame, "大小", self.size, 10, 100)
        self._create_scale(style_frame, "透明度", self.opacity, 0, 255)

        # 布局设置区域
        layout_frame = ttk.LabelFrame(parent, text="布局设置", padding=10)
        layout_frame.pack(fill=tk.X, pady=5)

        self._create_scale(layout_frame, "水平间距", self.horizontal_spacing, 10, 500)
        self._create_scale(layout_frame, "垂直间距", self.vertical_spacing, 10, 500)

        self.text_entry.bind("<FocusIn>", self.on_entry_focus_in)
        self.text_entry.bind("<FocusOut>", self.on_entry_focus_out)

    def _build_image_display(self):
        """构建图片显示区域"""
        self.image_label = ttk.Label(self.image_frame, background="#404040")
        self.image_label.pack(expand=True, fill=tk.BOTH)

    def _create_scale(self, parent, label, variable, from_, to):
        """创建统一风格的滑块控件"""
        frame = ttk.Frame(parent)
        frame.pack(fill=tk.X, pady=3)

        ttk.Label(frame, text=label, width=10).pack(side=tk.LEFT)
        ttk.Scale(
            frame,
            variable=variable,
            from_=from_,
            to=to,
            command=self.update_watermark
        ).pack(side=tk.LEFT, fill=tk.X, expand=True)

    def import_image(self):
        # 打开文件选择对话框
        self.image_path = filedialog.askopenfilename(filetypes=[("图片文件", "*.jpg;*.jpeg;*.png")])
        if self.image_path:
            try:
                # 打开原始图片
                self.original_image = Image.open(self.image_path)
                # 显示原始图片
                self.display_image = self.original_image.copy()
                self.show_image(self.display_image)
            except Exception as e:
                messagebox.showerror("错误", f"打开图片失败: {e}")

    def update_watermark(self, *args):
        if self.original_image:
            try:
                # 复制原始图片
                watermarked_image = self.original_image.copy()
                # 获取水印文本
                text = self.watermark_text.get()
                # 获取字体大小
                font_size = self.size.get()
                # 获取当前脚本所在目录
                script_dir = os.path.dirname(os.path.abspath(__file__))
                # 拼接字体文件路径
                font_path = os.path.join(script_dir, "myfont2.ttf")
                # 加载字体
                font = ImageFont.truetype(font_path, font_size)

                # 获取文本边界框
                left, top, right, bottom = ImageDraw.Draw(watermarked_image).textbbox((0, 0), text, font=font)
                text_width = right - left
                text_height = bottom - top

                # 获取间距
                horizontal_spacing = self.horizontal_spacing.get()
                vertical_spacing = self.vertical_spacing.get()

                # 获取透明度
                alpha = self.opacity.get()
                # 结合颜色和透明度
                final_color = self.watermark_color + (alpha,)

                # 创建透明画布（扩大到原始图片的2倍尺寸确保覆盖）
                expanded_size = (watermarked_image.width * 2, watermarked_image.height * 2)
                watermark = Image.new('RGBA', expanded_size, (0, 0, 0, 0))
                draw = ImageDraw.Draw(watermark)

                # 计算实际有效间距（确保最小为字体尺寸）
                effective_h_spacing = max(horizontal_spacing, text_width // 2)
                effective_v_spacing = max(vertical_spacing, text_height // 2)

                # 计算初始偏移量（从负边距开始绘制）
                start_x = -text_width
                start_y = -text_height

                # 计算需要覆盖的范围（包含旋转后的最大可能区域）
                row_offset = 0
                x = start_x
                while x < expanded_size[0] + text_width:
                    y = start_y + row_offset
                    while y < expanded_size[1] + text_height:
                        draw.text((x, y), text, fill=final_color, font=font)
                        y += text_height + effective_v_spacing
                    x += text_width + effective_h_spacing
                    row_offset = (row_offset + text_height // 2) % (text_height + effective_v_spacing)

                # 创建旋转后的水印
                rotated_watermark = watermark.rotate(
                    self.angle.get(),
                    expand=True,
                    resample=Image.BILINEAR
                )

                # 计算居中粘贴位置
                paste_position = (
                    (watermarked_image.width - rotated_watermark.width) // 2,
                    (watermarked_image.height - rotated_watermark.height) // 2
                )

                # 合并水印和原始图片
                watermarked_image = watermarked_image.convert('RGBA')
                watermarked_image.paste(
                    rotated_watermark,
                    paste_position,
                    rotated_watermark
                )

                # 更新显示图片
                self.display_image = watermarked_image
                self.show_image(self.display_image)
            except Exception as e:
                messagebox.showerror("错误", f"添加水印失败: {e}")

    def show_image(self, image):
        # 获取图片显示区域的大小
        max_width = self.image_frame.winfo_width()
        max_height = self.image_frame.winfo_height()
        width, height = image.size
        if width > max_width or height > max_height:
            ratio = min(max_width / width, max_height / height)
            new_width = int(width * ratio)
            new_height = int(height * ratio)
            image = image.resize((new_width, new_height), Image.LANCZOS)
        # 将 PIL 图片转换为 Tkinter 可用的图片对象
        photo = ImageTk.PhotoImage(image)
        # 更新图片显示区域
        self.image_label.config(image=photo)
        self.image_label.image = photo

    def export_image(self):
        if self.display_image:
            # 打开文件保存对话框
            save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                     filetypes=[("PNG 文件", "*.png"), ("JPEG 文件", "*.jpg;*.jpeg")])
            if save_path:
                try:
                    # 保存水印图片
                    self.display_image.save(save_path)
                    messagebox.showinfo("成功", "水印图片导出成功！")
                except Exception as e:
                    messagebox.showerror("错误", f"导出图片失败: {e}")

    def choose_color(self):
        # 打开颜色选择对话框
        color = colorchooser.askcolor()
        if color[0]:
            # 获取选择的颜色 RGB 值
            self.watermark_color = tuple(map(int, color[0]))
            # 更新水印效果
            self.update_watermark()

    def on_entry_focus_in(self, event):
        if self.text_entry.get() == "请输入水印内容":
            self.text_entry.delete(0, tk.END)

    def on_entry_focus_out(self, event):
        if not self.text_entry.get():
            self.text_entry.insert(0, "请输入水印内容")


if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()