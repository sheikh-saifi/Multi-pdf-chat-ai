css = '''
<style>
.chat-message {
    padding: 1.5rem;
    border-radius: 0.5rem;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: 1rem;
}
.chat-message.user {
    background-color: #2b313e;
}
.chat-message.bot {
    background-color: #475063;
}
.chat-message .avatar img {
    width: 78px;
    height: 78px;
    border-radius: 50%;
    object-fit: cover;
}
.chat-message .message {
    color: #fff;
    flex: 1;
    font-size: 1rem;
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/LX7QXny5/Whats-App-Image-2026-07-27-at-05-57-00.jpg">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.ibb.co/qLc73r9s/Whats-App-Image-2026-07-27-at-05-57-23.jpg">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''
