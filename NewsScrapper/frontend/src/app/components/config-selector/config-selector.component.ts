import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-config-selector',
  templateUrl: './config-selector.component.html',
  styleUrls: ['./config-selector.component.css']
})
export class ConfigSelectorComponent implements OnInit {
  llmProvider: string = 'gemini';

  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
    this.apiService.getConfig().subscribe(config => {
      this.llmProvider = config.llm_provider;
    });
  }

  updateProvider(): void {
    this.apiService.updateConfig({ llm_provider: this.llmProvider }).subscribe();
  }
}
