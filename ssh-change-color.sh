#!/bin/bash
set_profile() {
  /usr/bin/osascript -e "tell application \"Terminal\" to set current settings of first window to settings set \"$1\""
}

set_profile "Red Sands"
ssh $@
set_profile "Basic"