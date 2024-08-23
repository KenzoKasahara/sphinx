.. サンプルライブラリ documentation master file, created by
   sphinx-quickstart on Fri Aug 23 22:58:45 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

サンプルライブラリ documentation
================================

Add your content using ``reStructuredText`` syntax. See the
`reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
documentation for details.


------------------------------------------------
段落
------------------------------------------------

アスタリスク1つ: *テキスト* 強調(イタリック)

*test*

アスタリスク2つ: **テキスト** 強い強調(太文字)

**test**

バッククオート: ``テキスト`` コードサンプル

``test test``


------------------------------------------------
リストと引用のようなブロック
------------------------------------------------

* This is a bulleted list.
* It has two items, the second
  item uses two lines.

   * this is
   * a list

1. This is a numbered list.
2. It has two items too.
#. This is a numbered list.
#. It has two items too.

| These lines are
| broken exactly like in
| the source file.

------------------------------------------------
Literal blocks
------------------------------------------------

This is a normal text paragraph. The next paragraph is a code sample::

   It is not processed in any way, except
   that the indentation is removed.

   It can span multiple lines.

This is a normal text paragraph again.

------------------------------------------------
docktest
------------------------------------------------

>>> 1 + 1

------------------------------------------------
テーブル
------------------------------------------------

+------------------------+------------+----------+----------+
| Header row, column 1   | Header 2   | Header 3 | Header 4 |
| (header rows optional) |            |          |          |
+========================+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | column 4 |
+------------------------+------------+----------+----------+
| body row 2             | ...        | ...      |          |
+------------------------+------------+----------+----------+

=====  =====  =======
A      B      A and B
=====  =====  =======
False  False  False
True   False  False
False  True   False
True   True   True
=====  =====  =======

------------------------------------------------
ハイパーリンク
------------------------------------------------

`Link text <https://domain.invalid/>`_

This is a paragraph that contains `a link`_.

.. _a link: https://domain.invalid/

------------------------------------------------
セクション
------------------------------------------------

########################
Section 1
########################

========================
Section 2
========================

------------------------
Section 3
------------------------

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Section 4
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

""""""""""""""""""""""""
Section 5
""""""""""""""""""""""""

------------------------------------------------
:fieldname: Field content
------------------------------------------------

.. code-block::
   :caption: A cool example

       The output of this line starts with four spaces.

.. code-block::

       The output of this line has no spaces at the beginning.

------------------------------------------------
引用
------------------------------------------------

Lorem ipsum [Ref]_ dolor sit amet.

.. [Ref] Book or article reference, URL or whatever.

------------------------------------------------
コメント
------------------------------------------------

.. This is a comment.

..
   This whole indented block
   is a comment.

   Still in the comment.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   sample
