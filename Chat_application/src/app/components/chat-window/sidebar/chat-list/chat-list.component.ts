import { Component } from '@angular/core';

@Component({
  selector: 'app-chat-list',
  templateUrl: './chat-list.component.html',
  styleUrl: './chat-list.component.css'
})
export class ChatListComponent {
  items = [
    {
        "id": "2",
        "name": "Aarav",
        "prof_pic_url": "https://i.imgur.com/wxQFVlK.jpg",
        "is_online": false,
        "last_msg": "Hey, what's up?"
    },
    {
        "id": "3",
        "name": "Maya",
        "prof_pic_url": "https://i.imgur.com/XURRCWv.jpg",
        "is_online": true,
        "last_msg": "I'll call you later."
    },
    {
        "id": "4",
        "name": "Liam",
        "prof_pic_url": "https://i.imgur.com/ocLkshA.jpg",
        "is_online": false,
        "last_msg": "Happy Birthday!"
    },
    {
        "id": "5",
        "name": "Sophia",
        "prof_pic_url": "https://i.imgur.com/Mcd9z4F.jpg",
        "is_online": true,
        "last_msg": "Let's meet tomorrow."
    },
    {
        "id": "6",
        "name": "Noah",
        "prof_pic_url": "https://i.imgur.com/qenMrXK.jpg",
        "is_online": false,
        "last_msg": "Good night!"
    },
    {
        "id": "7",
        "name": "Olivia",
        "prof_pic_url": "https://i.imgur.com/ffHR2hp.jpg",
        "is_online": true,
        "last_msg": "I'm on my way."
    },
    {
        "id": "8",
        "name": "Aiden",
        "prof_pic_url": "https://i.imgur.com/tczIBp5.jpg",
        "is_online": false,
        "last_msg": "Thanks for the help!"
    },
    {
        "id": "9",
        "name": "Emma",
        "prof_pic_url": "https://i.imgur.com/Kh0DpF8.jpg",
        "is_online": true,
        "last_msg": "See you soon!"
    },
    {
        "id": "10",
        "name": "Lucas",
        "prof_pic_url": "https://i.imgur.com/W7XUjsF.jpg",
        "is_online": false,
        "last_msg": "Can you send me the file?"
    },
    {
        "id": "11",
        "name": "Isabella",
        "prof_pic_url": "https://i.imgur.com/cVQKSmg.jpg",
        "is_online": true,
        "last_msg": "I'll be there in 10 minutes."
    }
]
}
