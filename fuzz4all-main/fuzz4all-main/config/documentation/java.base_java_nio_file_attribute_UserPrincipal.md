# Interface UserPrincipal

**Source:** `java.base\java\nio\file\attribute\UserPrincipal.html`

### Class Description

```java
public interface
UserPrincipal

extends
Principal
```

A

Principal

representing an identity used to determine access rights
to objects in a file system.

On many platforms and file systems an entity requires appropriate access
rights or permissions in order to access objects in a file system. The
access rights are generally performed by checking the identity of the entity.
For example, on implementations that use Access Control Lists (ACLs) to
enforce privilege separation then a file in the file system may have an
associated ACL that determines the access rights of identities specified in
the ACL.

A

UserPrincipal

object is an abstract representation of an
identity. It has a

name

that is typically the username or
account name that it represents. User principal objects may be obtained using
a

UserPrincipalLookupService

, or returned by

FileAttributeView

implementations that provide access to identity related
attributes. For example, the

AclFileAttributeView

and

PosixFileAttributeView

provide access to a file's

owner

.

**All Superinterfaces:** Principal

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

*No entries found.*

### Additional Sections

#### Interface UserPrincipal

**All Superinterfaces:** Principal

**All Known Subinterfaces:** GroupPrincipal

```java
public interface
UserPrincipal

extends
Principal
```

A

Principal

representing an identity used to determine access rights
to objects in a file system.

On many platforms and file systems an entity requires appropriate access
rights or permissions in order to access objects in a file system. The
access rights are generally performed by checking the identity of the entity.
For example, on implementations that use Access Control Lists (ACLs) to
enforce privilege separation then a file in the file system may have an
associated ACL that determines the access rights of identities specified in
the ACL.

A

UserPrincipal

object is an abstract representation of an
identity. It has a

name

that is typically the username or
account name that it represents. User principal objects may be obtained using
a

UserPrincipalLookupService

, or returned by

FileAttributeView

implementations that provide access to identity related
attributes. For example, the

AclFileAttributeView

and

PosixFileAttributeView

provide access to a file's

owner

.

**Since:** 1.7

public interface

UserPrincipal

extends

Principal

A

Principal

representing an identity used to determine access rights
to objects in a file system.

On many platforms and file systems an entity requires appropriate access
rights or permissions in order to access objects in a file system. The
access rights are generally performed by checking the identity of the entity.
For example, on implementations that use Access Control Lists (ACLs) to
enforce privilege separation then a file in the file system may have an
associated ACL that determines the access rights of identities specified in
the ACL.

A

UserPrincipal

object is an abstract representation of an
identity. It has a

name

that is typically the username or
account name that it represents. User principal objects may be obtained using
a

UserPrincipalLookupService

, or returned by

FileAttributeView

implementations that provide access to identity related
attributes. For example, the

AclFileAttributeView

and

PosixFileAttributeView

provide access to a file's

owner

.

On many platforms and file systems an entity requires appropriate access
rights or permissions in order to access objects in a file system. The
access rights are generally performed by checking the identity of the entity.
For example, on implementations that use Access Control Lists (ACLs) to
enforce privilege separation then a file in the file system may have an
associated ACL that determines the access rights of identities specified in
the ACL.

A

UserPrincipal

object is an abstract representation of an
identity. It has a

name

that is typically the username or
account name that it represents. User principal objects may be obtained using
a

UserPrincipalLookupService

, or returned by

FileAttributeView

implementations that provide access to identity related
attributes. For example, the

AclFileAttributeView

and

PosixFileAttributeView

provide access to a file's

owner

.

A

UserPrincipal

object is an abstract representation of an
identity. It has a

name

that is typically the username or
account name that it represents. User principal objects may be obtained using
a

UserPrincipalLookupService

, or returned by

FileAttributeView

implementations that provide access to identity related
attributes. For example, the

AclFileAttributeView

and

PosixFileAttributeView

provide access to a file's

owner

.

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

