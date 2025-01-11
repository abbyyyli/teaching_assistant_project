from linebot.models import FollowEvent, UnfollowEvent, JoinEvent, LeaveEvent, BeaconEvent, TextSendMessage

def handle_follow_event(event, line_bot_api):
    """
    當用戶關注時觸發。
    """
    user_id = event.source.user_id
    welcome_message = "Thank you for following! Send 'start' to begin."
    line_bot_api.push_message(user_id, TextSendMessage(text=welcome_message))
    print(f"User {user_id} followed the bot.")

def handle_unfollow_event(event):
    """
    當用戶取消關注時觸發。
    """
    user_id = event.source.user_id
    print(f"User {user_id} unfollowed the bot.")

def handle_join_event(event, line_bot_api):
    """
    當 BOT 被加入群組或聊天室時觸發。
    """
    group_id = event.source.group_id
    welcome_message = "Hello, everyone! I'm here to assist. Type 'help' for more info."
    line_bot_api.push_message(group_id, TextSendMessage(text=welcome_message))
    print(f"Bot joined group {group_id}.")

def handle_leave_event(event):
    """
    當 BOT 被移除群組或聊天室時觸發。
    """
    group_id = event.source.group_id
    print(f"Bot was removed from group {group_id}.")

def handle_beacon_event(event, line_bot_api):
    """
    當 Beacon 訊號觸發時執行。
    """
    user_id = event.source.user_id
    beacon_message = "You triggered a Beacon event!"
    line_bot_api.push_message(user_id, TextSendMessage(text=beacon_message))
    print(f"User {user_id} triggered a Beacon event.")
