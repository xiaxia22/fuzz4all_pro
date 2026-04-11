# Interface AttributeView

**Source:** `java.base\java\nio\file\attribute\AttributeView.html`

### Class Description

```java
public interface
AttributeView
```

An object that provides a read-only or updatable

view

of non-opaque
values associated with an object in a filesystem. This interface is extended
or implemented by specific attribute views that define the attributes
supported by the view. A specific attribute view will typically define
type-safe methods to read or update the attributes that it supports.

**All Known Subinterfaces:** AclFileAttributeView

,

BasicFileAttributeView

,

DosFileAttributeView

,

FileAttributeView

,

FileOwnerAttributeView

,

FileStoreAttributeView

,

PosixFileAttributeView

,

UserDefinedFileAttributeView

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
name()

Returns the name of the attribute view.

**Returns:**
- the name of the attribute view

---

### Additional Sections

#### Interface AttributeView

**All Known Subinterfaces:** AclFileAttributeView

,

BasicFileAttributeView

,

DosFileAttributeView

,

FileAttributeView

,

FileOwnerAttributeView

,

FileStoreAttributeView

,

PosixFileAttributeView

,

UserDefinedFileAttributeView

```java
public interface
AttributeView
```

An object that provides a read-only or updatable

view

of non-opaque
values associated with an object in a filesystem. This interface is extended
or implemented by specific attribute views that define the attributes
supported by the view. A specific attribute view will typically define
type-safe methods to read or update the attributes that it supports.

**Since:** 1.7

public interface

AttributeView

An object that provides a read-only or updatable

view

of non-opaque
values associated with an object in a filesystem. This interface is extended
or implemented by specific attribute views that define the attributes
supported by the view. A specific attribute view will typically define
type-safe methods to read or update the attributes that it supports.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

name

()

Returns the name of the attribute view.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

name

()

Returns the name of the attribute view.

---

#### Method Summary

Returns the name of the attribute view.

============ METHOD DETAIL ==========

- Method Detail

- name

```java
String
name()
```

Returns the name of the attribute view.

**Returns:** the name of the attribute view

Method Detail

- name

```java
String
name()
```

Returns the name of the attribute view.

**Returns:** the name of the attribute view

---

#### Method Detail

name

```java
String
name()
```

Returns the name of the attribute view.

**Returns:** the name of the attribute view

---

#### name

String

name()

Returns the name of the attribute view.

---

