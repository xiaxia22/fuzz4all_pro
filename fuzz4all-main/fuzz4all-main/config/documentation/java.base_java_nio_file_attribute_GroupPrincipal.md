# Interface GroupPrincipal

**Source:** `java.base\java\nio\file\attribute\GroupPrincipal.html`

### Class Description

```java
public interface
GroupPrincipal

extends
UserPrincipal
```

A

UserPrincipal

representing a

group identity

, used to
determine access rights to objects in a file system. The exact definition of
a group is implementation specific, but typically, it represents an identity
created for administrative purposes so as to determine the access rights for
the members of the group. Whether an entity can be a member of multiple
groups, and whether groups can be nested, are implementation specified and
therefore not specified.

**All Superinterfaces:** Principal

,

UserPrincipal

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

*No entries found.*

### Additional Sections

#### Interface GroupPrincipal

**All Superinterfaces:** Principal

,

UserPrincipal

```java
public interface
GroupPrincipal

extends
UserPrincipal
```

A

UserPrincipal

representing a

group identity

, used to
determine access rights to objects in a file system. The exact definition of
a group is implementation specific, but typically, it represents an identity
created for administrative purposes so as to determine the access rights for
the members of the group. Whether an entity can be a member of multiple
groups, and whether groups can be nested, are implementation specified and
therefore not specified.

**Since:** 1.7
**See Also:** UserPrincipalLookupService.lookupPrincipalByGroupName(java.lang.String)

public interface

GroupPrincipal

extends

UserPrincipal

A

UserPrincipal

representing a

group identity

, used to
determine access rights to objects in a file system. The exact definition of
a group is implementation specific, but typically, it represents an identity
created for administrative purposes so as to determine the access rights for
the members of the group. Whether an entity can be a member of multiple
groups, and whether groups can be nested, are implementation specified and
therefore not specified.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in interface java.security.

Principal

equals

,

getName

,

hashCode

,

implies

,

toString

Method Summary

- Methods declared in interface java.security.

Principal

equals

,

getName

,

hashCode

,

implies

,

toString

---

#### Method Summary

Methods declared in interface java.security.

Principal

equals

,

getName

,

hashCode

,

implies

,

toString

---

