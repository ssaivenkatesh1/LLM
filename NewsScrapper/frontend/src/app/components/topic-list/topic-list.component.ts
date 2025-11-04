import { Component, Input } from '@angular/core';
import { Topic } from '../../models/topic.model';

@Component({
  selector: 'app-topic-list',
  templateUrl: './topic-list.component.html',
  styleUrls: ['./topic-list.component.css']
})
export class TopicListComponent {
  @Input() topics: Topic[] = [];
}
