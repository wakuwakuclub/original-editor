# original-editor

## Quick Start
### node.jsのインストール
electronを動作させるためにはnode.jsというものが必要です。  
下のリンクを踏むとWindows版のダウンロードが始まります。ダウンロード後、指示に従ってインストールをしてください。  
**[node.js-10.16.3](https://nodejs.org/dist/v10.16.3/node-v10.16.3-x64.msi)**

### リポジトリのclone
GitとGitHun Desktopをインストールして、右上の**Clone or download**ボタンを押して**Opne in Desktop**を選択してください。自動でGitHub Desktopが起動してcloneが始まります。

### Download Zip
もしGitの導入が面倒な場合、**Clone or download** の **Download Zip** でも構いません。  
その場合解凍後、そのフォルダに移動してください。

### electronの準備
```bash
# はじめにoriginal-editorに移動する
# -------------------
# electronのインストール
npm i -D electron

# electron-localshortcutのインストール
npm i -D electron-localshortcut

# ファイルの実行
npm run start
```
---

## 説明
わくわく倶楽部主催ハンズオン「electronでエディタを作ろう」のリポジトリ

---

## 元リポジトリ
[テキストエディターを作ってElectronの基礎を学ぼう！ HTML5でPCアプリ開発入門　のデモアプリ](https://github.com/ics-creative/150819_electron_text_editor)

---

## 参考リンク
### electron
+ [最新版で学ぶElectron入門 ウェブ技術でPCアプリを開発しよう](https://ics.media/entry/7298/)
### editor
+ [テキストエディターを作ってElectronの基礎を学ぼう！HTML5でデスクトップアプリケーション開発入門](https://ics.media/entry/8401/)
### shortcut
+ [Electronアプリは、まずelectron-localshortcut入れて、Command+R、Command+Wを潰すのがセオリーだと思う](https://taku-o.hatenablog.jp/entry/20181020/1540026153)