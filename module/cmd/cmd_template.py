# CMD模板

ps_cmd_str = "ps -ef | grep %s | grep -v grep | grep -v git | awk {'print $2, $5, $7, $9'} "
