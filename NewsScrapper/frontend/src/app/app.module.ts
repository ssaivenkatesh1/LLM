import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { HomeComponent } from './components/home/home.component';
import { TopicListComponent } from './components/topic-list/topic-list.component';
import { ConfigSelectorComponent } from './components/config-selector/config-selector.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    TopicListComponent,
    ConfigSelectorComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
