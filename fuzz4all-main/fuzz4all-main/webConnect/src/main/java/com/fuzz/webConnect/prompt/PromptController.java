package com.fuzz.webConnect.prompt;

import com.fuzz.webConnect.storage.FileStorageService;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

import java.util.List;

@RestController
@RequestMapping("/api/prompts")
public class PromptController {

    private final PromptRepository promptRepository;
    private final FileStorageService fileStorageService;

    public PromptController(PromptRepository promptRepository, FileStorageService fileStorageService) {
        this.promptRepository = promptRepository;
        this.fileStorageService = fileStorageService;
    }

    @GetMapping
    public List<PromptEntity> list() {
        return promptRepository.findAll();
    }

    @PostMapping
    public PromptEntity create(@RequestBody PromptEntity prompt) {
        return promptRepository.save(prompt);
    }

    @PostMapping("/upload")
    public PromptEntity upload(@RequestParam("file") MultipartFile file) {
        String path = fileStorageService.store(file, "prompts");
        PromptEntity entity = new PromptEntity();
        entity.setName(file.getOriginalFilename() == null ? "prompt" : file.getOriginalFilename());
        entity.setFilePath(path);
        return promptRepository.save(entity);
    }

    @DeleteMapping("/{id}")
    @ResponseStatus(HttpStatus.NO_CONTENT)
    public void delete(@PathVariable Long id) {
        promptRepository.deleteById(id);
    }
}
