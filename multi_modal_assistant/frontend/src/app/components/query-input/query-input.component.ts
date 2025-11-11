import { Component, EventEmitter, Output } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-query-input',
  standalone: true,
  imports: [FormsModule, CommonModule],
  templateUrl: './query-input.component.html',
  styleUrls: ['./query-input.component.css']
})
export class QueryInputComponent {
  @Output() querySubmitted = new EventEmitter<string>();
  query = '';

  submitQuery() {
    this.querySubmitted.emit(this.query);
  }
}