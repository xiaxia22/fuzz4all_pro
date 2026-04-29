package com.fuzz.webConnect.storage;

import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.util.UUID;

@Service
public class FileStorageService {

    private final Path rootDir;

    public FileStorageService() {
        this.rootDir = Paths.get("uploads");
    }

    public String store(MultipartFile file, String subDir) {
        try {
            Path dir = rootDir.resolve(subDir);
            Files.createDirectories(dir);

            String originalName = file.getOriginalFilename();
            String safeName = (originalName == null || originalName.isBlank()) ? "file.bin" : originalName;
            String storedName = UUID.randomUUID() + "_" + safeName;

            Path target = dir.resolve(storedName);
            Files.copy(file.getInputStream(), target, StandardCopyOption.REPLACE_EXISTING);

            return target.toString().replace('\\', '/');
        } catch (IOException e) {
            throw new RuntimeException("file save failed", e);
        }
    }
}
