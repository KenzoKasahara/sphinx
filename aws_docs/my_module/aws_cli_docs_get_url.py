import urllib.request
import os
import re
import json

from bs4 import BeautifulSoup

from .deco_prcessing_time import timeit


class GetAwsCliDocs(object):
    """
    AWS CLIのドキュメントページから指定したキーワードを含むリンクのタイトルとURIを取得する
    """

    def __init__(self, url: str, search_word: str):
        """
        Args:
        --------------------
            url : str
                AWS CLIのドキュメントページのURL
            search_word : str
                検索キーワード
        """
        self.url = url
        self.link_uri = f".*{search_word}.*?/index.html"

    @timeit
    def fetch_html(self, url: str) -> str:
        """
        Returns:
        --------------------
            type: str
            検索キーワードを含むリンクのタイトルとURIを取得したHTMLを返す
        """
        if url == "":
            url = self.url
        else:
            url = url

        with urllib.request.urlopen(url) as res:
            html = res.read().decode()
        return html

    @timeit
    def get_title_and_uris(self, html: str, api_name: str) -> dict:
        """_summary_

        Args:
        --------------------
            html : str
                検索キーワードを含むリンクのタイトルとURIを取得したHTML
            api_name : str
                API名

        Returns:
        --------------------
            type: list[dict[str, Any]]
            タイトルとURIを取得した辞書のリストを返す
        """
        common_uri = "https://awscli.amazonaws.com/v2/documentation/api/latest/"
        result = []
        soup = BeautifulSoup(html, "html.parser")

        if api_name == "":
            a_tags = soup.find_all("a",
                                   attrs={
                                       "href": re.compile(f'{self.link_uri}')
                                    })
        else:
            common_uri = f"{common_uri}/reference/{api_name}/"
            a_tags = soup.find_all(["li", "a"],
                                   class_='reference internal',
                                   attrs={"href": re.compile('\.html$')})

        title_list = [title.get_text() for title in a_tags]
        uris = [uri.get("href") for uri in a_tags]
        index = ['title', 'uri']

        for title, uri in zip(title_list, uris):
            result.append({index[0]: title, index[1]: common_uri + uri})

        return result

    @timeit
    def output_json(self,
                    output_dir: str,
                    search_word: str,
                    title: str,
                    dict_data: dict):
        """
        検索キーワードと同一名のフォルダを作成し、
        AWS CLI ドキュメントのタイトルとURL情報を保持したjsonを出力する

        Args:
        --------------------
            output_dir : str
                出力先のディレクトリパス
            search_word : str
                検索キーワード
            title : str
                ファイルタイトル
            dict_data : dict
                タイトルとURIを取得した辞書
        """
        if title == "":
            title = search_word
            output_path = f"{output_dir}/{search_word}/links_{search_word}.json"
        else:
            title = title
            output_path = f"{output_dir}/{search_word}/api_{title}.json"

        os.makedirs(f"{output_dir}/{search_word}", exist_ok=True)
        with open(output_path, "w", encoding="utf_8") as f:
            f.write(json.dumps(dict_data, indent=4))
