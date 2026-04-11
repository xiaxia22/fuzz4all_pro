# Interface PathMatcher

**Source:** `java.base\java\nio\file\PathMatcher.html`

### Class Description

```java
@FunctionalInterface

public interface
PathMatcher
```

An interface that is implemented by objects that perform match operations on
paths.

**Functional Interface:** This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean matches​(
Path
path)

Tells if given path matches this matcher's pattern.

**Parameters:**
- path

- the path to match

**Returns:**
- true

if, and only if, the path matches this
matcher's pattern

---

### Additional Sections

#### Interface PathMatcher

**Functional Interface:** This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

```java
@FunctionalInterface

public interface
PathMatcher
```

An interface that is implemented by objects that perform match operations on
paths.

**Since:** 1.7
**See Also:** FileSystem.getPathMatcher(java.lang.String)

,

Files.newDirectoryStream(Path,String)

@FunctionalInterface

public interface

PathMatcher

An interface that is implemented by objects that perform match operations on
paths.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

matches

​(

Path

path)

Tells if given path matches this matcher's pattern.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

matches

​(

Path

path)

Tells if given path matches this matcher's pattern.

---

#### Method Summary

Tells if given path matches this matcher's pattern.

============ METHOD DETAIL ==========

- Method Detail

- matches

```java
boolean matches​(
Path
path)
```

Tells if given path matches this matcher's pattern.

**Parameters:** path

- the path to match
**Returns:** true

if, and only if, the path matches this
matcher's pattern

Method Detail

- matches

```java
boolean matches​(
Path
path)
```

Tells if given path matches this matcher's pattern.

**Parameters:** path

- the path to match
**Returns:** true

if, and only if, the path matches this
matcher's pattern

---

#### Method Detail

matches

```java
boolean matches​(
Path
path)
```

Tells if given path matches this matcher's pattern.

**Parameters:** path

- the path to match
**Returns:** true

if, and only if, the path matches this
matcher's pattern

---

#### matches

boolean matches​(

Path

path)

Tells if given path matches this matcher's pattern.

---

