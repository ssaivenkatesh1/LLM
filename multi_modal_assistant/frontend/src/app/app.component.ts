import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { ImageUploadComponent } from './components/image-upload/image-upload.component';
import { QueryInputComponent } from './components/query-input/query-input.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    RouterOutlet,
    FormsModule,
    CommonModule,
    ImageUploadComponent,
    QueryInputComponent
  ],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Multimodal Assistant';
  query = '';
  imageFile: File | null = null;
  result: any = null;
  isLoading = false;
  error: string | null = null;

  constructor(private http: HttpClient) {}

  onImageSelected(file: File) {
    this.imageFile = file;
  }

  onQuerySubmitted(query: string) {
    this.query = query;
    this.submitQuery();
  }

  submitQuery() {
    if (!this.query && !this.imageFile) {
      this.error = 'Please enter a query or upload an image.';
      return;
    }

    const formData = new FormData();
    formData.append('query', this.query);
    if (this.imageFile) {
      if (!this.imageFile.type.startsWith('image/')) {
        this.error = 'Invalid file type. Please upload an image.';
        return;
      }
      formData.append('image', this.imageFile, this.imageFile.name);
    }

    this.isLoading = true;
    this.result = null;
    this.error = null;

    this.http.post<any>('http://localhost:8000/api/query', formData).subscribe(
      (res) => {
        this.result = res;
        this.isLoading = false;
      },
      (err) => {
        console.error(err);
        this.error = err?.error?.detail || 'An error occurred while processing your request. Please try again later.';
        this.isLoading = false;
      }
    );
  }
}
