from diaries.AbstractDiary import AbstractDiary


class WapponDiary(AbstractDiary):
    def get_date(self) -> str:
        return "2025-10-15"

    def get_summary(self) -> str:
        RESET = "\033[0m"
        GRAY = "\033[90m"
        RED = "\033[31m"
        ITALIC = "\033[3m"

        def quote(text: str) -> str:
            return f"{ITALIC}{GRAY}│ {text}{RESET}"

        return "\n".join(
            [
                "数日前から闘っていたものがようやく終わりを迎えた.",
                "",
                quote("電卓が使えないとか・・・"),
                "  —— ああ, 確かに打ちミスはした.  ただ, 計算技術検定を持っているのに, そんなことを言われてしまっては, 何か胸に刺さるものがある.",
                "",
                quote("もう少しです。"),
                "  —— 一筋の光が見えた気がした.  そう, もう少しで終わる.  そう思った.",
                "",
                quote("もう少しでした。"),
                "  —— なんだ？  過去形になったとて, 何も変わらない結果が辛い.",
                "",
                quote("１つ楽をしようとミスしていますが、"),
                "  —— 自身の怠惰さを指摘されている.  ああそうだ, 俺は楽をしようとしてミスをしたんだ.",
                "",
                "気づけば, 何往復もしていた.  ようやく今日, “神の審判” を得てすべてを終わらすことができた.",
                f"{RED}では,{RESET}",
                "",
            ]
        )

    def get_author(self) -> str:
        return "Wappon"
