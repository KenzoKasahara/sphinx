import os

from my_module.aws_cli_docs_get_url import GetAwsCliDocs


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(CURRENT_DIR, "aws_cli_info")

urls = [
    # "https://docs.aws.amazon.com/cli/latest/",
    "https://awscli.amazonaws.com/v2/documentation/api/latest/index.html",
]


def get_related_section(type: str, urls: list, search_word: str = "") -> list:
    """
    任意のAWS CLIのドキュメントページURLの情報をJSONファイルに出力する

    Args:
    --------------------
        type : str
            取得する情報の種類
        urls : list
            取得する情報のURL
        search_word : str
            検索キーワード

    Returns:
    --------------------
        type: list
            タイトルとURIを取得した辞書のリストを返す
    """
    for url in urls:
        if type == "related":
            title = ""
            api_name = ""
            uri = ""
        elif type == "api":
            title = url["title"]
            api_name = url["title"]
            uri = url["uri"]

        print(f"{'*'*30} ...処理中... {'*'*30} ")
        print(f"type: {type}, api_name: {api_name}, uri: {uri}")

        aws_cli_docs = GetAwsCliDocs(url, search_word)
        html = aws_cli_docs.fetch_html(uri)
        title_and_uris = aws_cli_docs.get_title_and_uris(html, api_name)

        if title_and_uris:
            aws_cli_docs.output_json(OUTPUT_DIR,
                                     search_word,
                                     title,
                                     title_and_uris)

    return title_and_uris


if __name__ == "__main__":
    print("検索キーワードを入力してください >>>")
    search_word = str(input())

    if not search_word:
        print("キーワードが空のため処理を終了します")
    else:
        # 検索キーワードを含むリンクのタイトルとURIを取得
        type = "related"
        title_and_uris = get_related_section(type, urls, search_word)

        # APIのドキュメントページリンク取得
        type = "api"
        get_related_section(type, title_and_uris, search_word)

    print(f"{'*'*74} ")
    print("処理が完了しました")
