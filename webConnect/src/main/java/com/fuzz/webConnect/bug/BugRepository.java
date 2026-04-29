package com.fuzz.webConnect.bug;

import org.springframework.data.jpa.repository.JpaRepository;

public interface BugRepository extends JpaRepository<BugEntity, Long> {
}
