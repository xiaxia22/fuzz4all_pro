package com.fuzz.webConnect.code;

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
@RequestMapping("/api/codes")
public class CodeController {

    private final CodeRepository codeRepository;
    private final FileStorageService fileStorageService;

    public CodeController(CodeRepository codeRepository, FileStorageService fileStorageService) {
        this.codeRepository = codeRepository;
        this.fileStorageService = fileStorageService;
    }

    @GetMapping
    public List<CodeEntity> list() {
        return codeRepository.findAll();
    }

    @PostMapping
    public CodeEntity create(@RequestBody CodeEntity code) {
        return codeRepository.save(code);
    }

    @PostMapping("/upload")
    public CodeEntity upload(@RequestParam("file") MultipartFile file) {
        String path = fileStorageService.store(file, "codes");
        CodeEntity entity = new CodeEntity();
        entity.setName(file.getOriginalFilename() == null ? "code" : file.getOriginalFilename());
        entity.setFilePath(path);
        return codeRepository.save(entity);
    }

    @DeleteMapping("/{id}")
    @ResponseStatus(HttpStatus.NO_CONTENT)
    public void delete(@PathVariable Long id) {
        codeRepository.deleteById(id);
    }
}
