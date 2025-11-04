import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private apiUrl = 'http://localhost:8000'; // Backend URL

  constructor(private http: HttpClient) { }

  getTopics(): Observable<any> {
    return this.http.get(`${this.apiUrl}/topics`);
  }

  scrape(): Observable<any> {
    console.log("Scrape will be called")
    return this.http.post(`${this.apiUrl}/scrape`, {});
  }

  getConfig(): Observable<any> {
    return this.http.get(`${this.apiUrl}/config`);
  }

  updateConfig(config: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/config`, config);
  }
}
