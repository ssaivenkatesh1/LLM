import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../services/api.service';
import { finalize } from 'rxjs/operators';
import { Topic } from '../../models/topic.model';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  topics: Topic[] = [];
  isLoading = false;
  error: string | null = null;

  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
    this.loadTopics();
  }

  loadTopics(): void {
    this.isLoading = true;
    this.error = null;
    this.apiService.getTopics()
      .pipe(finalize(() => this.isLoading = false))
      .subscribe({
        next: (data) => this.topics = data,
        error: (err) => this.error = 'Failed to load topics.'
      });
  }

  refreshTopics(): void {
    console.log("refreshTopics() called");
    this.isLoading = true;
    this.error = null;
    this.apiService.scrape()
      .pipe(finalize(() => this.loadTopics()))
      .subscribe({
        error: (err) => this.error = 'Failed to refresh topics.'
      });
  }
}
