# Interface StandardJavaFileManager.PathFactory

**Source:** `java.compiler\javax\tools\StandardJavaFileManager.PathFactory.html`

### Class Description

```java
public static interface
StandardJavaFileManager.PathFactory
```

Factory to create

Path

objects from strings.

**Enclosing interface:** StandardJavaFileManager

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Path
getPath​(
String
first,

String
... more)

Converts a path string, or a sequence of strings that when joined form a path string, to a Path.

**Parameters:**
- first

- the path string or initial part of the path string
- more

- additional strings to be joined to form the path string

**Returns:**
- the resulting

Path

---

### Additional Sections

#### Interface StandardJavaFileManager.PathFactory

**Enclosing interface:** StandardJavaFileManager

```java
public static interface
StandardJavaFileManager.PathFactory
```

Factory to create

Path

objects from strings.

**Since:** 9

public static interface

StandardJavaFileManager.PathFactory

Factory to create

Path

objects from strings.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Path

getPath

​(

String

first,

String

... more)

Converts a path string, or a sequence of strings that when joined form a path string, to a Path.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Path

getPath

​(

String

first,

String

... more)

Converts a path string, or a sequence of strings that when joined form a path string, to a Path.

---

#### Method Summary

Converts a path string, or a sequence of strings that when joined form a path string, to a Path.

============ METHOD DETAIL ==========

- Method Detail

- getPath

```java
Path
getPath​(
String
first,

String
... more)
```

Converts a path string, or a sequence of strings that when joined form a path string, to a Path.

**Parameters:** first

- the path string or initial part of the path string
**Parameters:** more

- additional strings to be joined to form the path string
**Returns:** the resulting

Path

Method Detail

- getPath

```java
Path
getPath​(
String
first,

String
... more)
```

Converts a path string, or a sequence of strings that when joined form a path string, to a Path.

**Parameters:** first

- the path string or initial part of the path string
**Parameters:** more

- additional strings to be joined to form the path string
**Returns:** the resulting

Path

---

#### Method Detail

getPath

```java
Path
getPath​(
String
first,

String
... more)
```

Converts a path string, or a sequence of strings that when joined form a path string, to a Path.

**Parameters:** first

- the path string or initial part of the path string
**Parameters:** more

- additional strings to be joined to form the path string
**Returns:** the resulting

Path

---

#### getPath

Path

getPath​(

String

first,

String

... more)

Converts a path string, or a sequence of strings that when joined form a path string, to a Path.

---

