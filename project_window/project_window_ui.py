import sys

try:
    from PyQt5.QtWidgets import (
        QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
        QScrollArea, QMainWindow, QSizePolicy
    )
    from PyQt5.QtCore import Qt
    PYQT5_AVAILABLE = True
except Exception as e:  # noqa: E722
    PYQT5_AVAILABLE = False
    print("PyQt5 is required to run this UI:", e)


class SceneWidget(QWidget):
    """Simple widget representing a Scene summary."""

    COLORS = [
        "#f8d7da",
        "#d4edda",
        "#d1ecf1",
        "#fff3cd",
        "#d6d8d9",
    ]

    def __init__(self, name, index):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)
        label = QLabel(name)
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        self.setFixedHeight(300)
        color = self.COLORS[index % len(self.COLORS)]
        self.setStyleSheet(
            f"border: 1px solid gray; border-radius: 4px; background-color: {color};"
        )


class ChapterWidget(QWidget):
    """Widget for a Chapter containing multiple scenes."""

    def __init__(self, name, scenes):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        title = QLabel(f"<b>{name}</b>")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        for idx, scene in enumerate(scenes):
            layout.addWidget(SceneWidget(scene, idx))
        layout.addStretch()
        self.setFixedWidth(400)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.setStyleSheet("border: 1px solid black; background-color: #ffffff;")


class ActWidget(QWidget):
    """Widget representing an Act with horizontally scrollable chapters."""

    def __init__(self, name, chapters):
        super().__init__()
        outer_layout = QVBoxLayout(self)
        outer_layout.setContentsMargins(10, 10, 10, 10)
        title = QLabel(f"<h2>{name}</h2>")
        outer_layout.addWidget(title)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        chapter_container = QWidget()
        h_layout = QHBoxLayout(chapter_container)
        h_layout.setContentsMargins(0, 0, 0, 0)
        for chap in chapters:
            h_layout.addWidget(ChapterWidget(chap["name"], chap["scenes"]))
        h_layout.addStretch()
        scroll.setWidget(chapter_container)
        outer_layout.addWidget(scroll)
        self.setFixedHeight(600)
        self.setStyleSheet("background-color: #ececec; border: 1px solid #aaaaaa;")


class ContentViewPanel(QWidget):
    """Main panel displaying Acts, Chapters, and Scenes."""

    def __init__(self, data):
        super().__init__()
        self.data = data
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)

        acts_scroll = QScrollArea()
        acts_scroll.setWidgetResizable(True)
        acts_container = QWidget()
        acts_layout = QVBoxLayout(acts_container)
        acts_layout.setContentsMargins(0, 0, 0, 0)
        for act in self.data:
            acts_layout.addWidget(ActWidget(act["name"], act["chapters"]))
        acts_layout.addStretch()
        acts_scroll.setWidget(acts_container)
        main_layout.addWidget(acts_scroll)

        # Thumbnail area
        thumb_widget = QWidget()
        thumb_layout = QHBoxLayout(thumb_widget)
        thumb_layout.setContentsMargins(5, 5, 5, 5)
        for act in self.data:
            for chap in act["chapters"]:
                box = QLabel(chap["name"])
                box.setAlignment(Qt.AlignCenter)
                box.setFixedSize(80, 40)
                box.setStyleSheet(
                    "border: 1px solid gray; background-color: lightgray; margin-right: 5px;"
                )
                thumb_layout.addWidget(box)
        thumb_layout.addStretch()
        main_layout.addWidget(thumb_widget)


# Sample data with 2 Acts, 4 Chapters each, 2 Scenes per Chapter
SAMPLE_DATA = [
    {
        "name": "Act 1",
        "chapters": [
            {"name": f"Chapter {i+1}", "scenes": [f"Scene A{i+1}.1", f"Scene A{i+1}.2"]}
            for i in range(4)
        ],
    },
    {
        "name": "Act 2",
        "chapters": [
            {"name": f"Chapter {i+1}", "scenes": [f"Scene B{i+1}.1", f"Scene B{i+1}.2"]}
            for i in range(4)
        ],
    },
]


def main():
    if not PYQT5_AVAILABLE:
        return
    app = QApplication(sys.argv)
    window = QMainWindow()
    panel = ContentViewPanel(SAMPLE_DATA)
    window.setCentralWidget(panel)
    window.showMaximized()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
