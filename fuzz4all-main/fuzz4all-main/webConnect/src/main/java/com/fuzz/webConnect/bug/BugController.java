package com.fuzz.webConnect.bug;

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
@RequestMapping("/api/bugs")
public class BugController {

    private final BugRepository bugRepository;
    private final FileStorageService fileStorageService;

    public BugController(BugRepository bugRepository, FileStorageService fileStorageService) {
        this.bugRepository = bugRepository;
        this.fileStorageService = fileStorageService;
    }

    @GetMapping
    public List<BugEntity> list() {
        return bugRepository.findAll();
    }

    @PostMapping
    public BugEntity create(@RequestBody BugEntity bug) {
        return bugRepository.save(bug);
    }

    @PostMapping("/upload")
    public BugEntity upload(
            @RequestParam("name") String name,
            @RequestParam("description") String description,
            @RequestParam(value = "image", required = false) MultipartFile image
    ) {
        BugEntity entity = new BugEntity();
        entity.setName(name);
        entity.setDescription(description);

        if (image != null && !image.isEmpty()) {
            String imagePath = fileStorageService.store(image, "bugs");
            entity.setImagePath(imagePath);
        }

        return bugRepository.save(entity);
    }

    @DeleteMapping("/{id}")
    @ResponseStatus(HttpStatus.NO_CONTENT)
    public void delete(@PathVariable Long id) {
        bugRepository.deleteById(id);
    }
}
