#!/bin/bash

# デフォルトカラー
BG_COLOR_DEFAULT='111'

# 背景変更 (iTerm2)
function bg_color_change(){
  echo -ne '\033]1337;SetColors=bg='"$1"'\a'
}

# sshから抜けた際に背景を戻す (iTerm2)
function bg_color_default(){
  bg_color_change $BG_COLOR_DEFAULT
}

# 背景変更
bg_color_change '993d3d'

# ssh接続
ssh "$@";

# sshから抜けた際に背景を戻す
bg_color_default
