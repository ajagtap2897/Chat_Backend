import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { provideAnimationsAsync } from '@angular/platform-browser/animations/async';
import { ChatWindowComponent } from './components/chat-window/chat-window.component';
import { MainAreaComponent } from './components/chat-window/main-area/main-area.component';
import { SidebarComponent } from './components/chat-window/sidebar/sidebar.component';
import { ChatHeaderComponent } from './components/chat-window/main-area/chat-header/chat-header.component';
import { ChatHistoryComponent } from './components/chat-window/main-area/chat-history/chat-history.component';
import { ChatMessageComponent } from './components/chat-window/main-area/chat-message/chat-message.component';
import { SearchComponent } from './components/chat-window/sidebar/search/search.component';
import { ChatListComponent } from './components/chat-window/sidebar/chat-list/chat-list.component';
import { ChatComponent } from './components/chat-window/sidebar/chat-list/chat/chat.component';

import {MatSidenavModule} from '@angular/material/sidenav';
import {MatButtonModule} from '@angular/material/button';
import {MatToolbarModule} from '@angular/material/toolbar';
import {MatFormFieldModule} from '@angular/material/form-field';
import {MatIconModule} from '@angular/material/icon';
import {MatInputModule} from '@angular/material/input';
import {MatCardModule} from '@angular/material/card';

@NgModule({
  declarations: [
    AppComponent,
    ChatWindowComponent,
    MainAreaComponent,
    SidebarComponent,
    ChatHeaderComponent,
    ChatHistoryComponent,
    ChatMessageComponent,
    SearchComponent,
    ChatListComponent,
    ChatComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    MatSidenavModule, 
    MatToolbarModule, 
    MatButtonModule, 
    MatIconModule, 
    MatFormFieldModule, 
    MatInputModule, 
    MatIconModule,
    MatCardModule 
  ],
  providers: [
    provideAnimationsAsync()
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
