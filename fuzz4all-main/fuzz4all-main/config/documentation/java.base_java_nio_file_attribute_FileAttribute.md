# Interface FileAttribute<T>

**Source:** `java.base\java\nio\file\attribute\FileAttribute.html`

### Class Description

```java
public interface
FileAttribute<T>
```

An object that encapsulates the value of a file attribute that can be set
atomically when creating a new file or directory by invoking the

createFile

or

createDirectory

methods.

**Type Parameters:** T

- The type of the file attribute value

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
name()

Returns the attribute name.

**Returns:**
- The attribute name

---

#### T
value()

Returns the attribute value.

**Returns:**
- The attribute value

---

### Additional Sections

#### Interface FileAttribute<T>

**Type Parameters:** T

- The type of the file attribute value

```java
public interface
FileAttribute<T>
```

An object that encapsulates the value of a file attribute that can be set
atomically when creating a new file or directory by invoking the

createFile

or

createDirectory

methods.

**Since:** 1.7
**See Also:** PosixFilePermissions.asFileAttribute(java.util.Set<java.nio.file.attribute.PosixFilePermission>)

public interface

FileAttribute<T>

An object that encapsulates the value of a file attribute that can be set
atomically when creating a new file or directory by invoking the

createFile

or

createDirectory

methods.

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

Returns the attribute name.

T

value

()

Returns the attribute value.

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

Returns the attribute name.

T

value

()

Returns the attribute value.

---

#### Method Summary

Returns the attribute name.

Returns the attribute value.

============ METHOD DETAIL ==========

- Method Detail

- name

```java
String
name()
```

Returns the attribute name.

**Returns:** The attribute name

- value

```java
T
value()
```

Returns the attribute value.

**Returns:** The attribute value

Method Detail

- name

```java
String
name()
```

Returns the attribute name.

**Returns:** The attribute name

- value

```java
T
value()
```

Returns the attribute value.

**Returns:** The attribute value

---

#### Method Detail

name

```java
String
name()
```

Returns the attribute name.

**Returns:** The attribute name

---

#### name

String

name()

Returns the attribute name.

value

```java
T
value()
```

Returns the attribute value.

**Returns:** The attribute value

---

#### value

T

value()

Returns the attribute value.

---

