# Interface OptionChecker

**Source:** `java.compiler\javax\tools\OptionChecker.html`

### Class Description

```java
public interface
OptionChecker
```

Interface for recognizing options.

**All Known Subinterfaces:** DocumentationTool

,

JavaCompiler

,

JavaFileManager

,

StandardJavaFileManager

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### int isSupportedOption​(
String
option)

Determines if the given option is supported and if so, the
number of arguments the option takes.

**Parameters:**
- option

- an option

**Returns:**
- the number of arguments the given option takes or -1 if
the option is not supported

---

### Additional Sections

#### Interface OptionChecker

**All Known Subinterfaces:** DocumentationTool

,

JavaCompiler

,

JavaFileManager

,

StandardJavaFileManager

**All Known Implementing Classes:** ForwardingJavaFileManager

```java
public interface
OptionChecker
```

Interface for recognizing options.

**Since:** 1.6

public interface

OptionChecker

Interface for recognizing options.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

isSupportedOption

​(

String

option)

Determines if the given option is supported and if so, the
number of arguments the option takes.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

isSupportedOption

​(

String

option)

Determines if the given option is supported and if so, the
number of arguments the option takes.

---

#### Method Summary

Determines if the given option is supported and if so, the
number of arguments the option takes.

============ METHOD DETAIL ==========

- Method Detail

- isSupportedOption

```java
int isSupportedOption​(
String
option)
```

Determines if the given option is supported and if so, the
number of arguments the option takes.

**Parameters:** option

- an option
**Returns:** the number of arguments the given option takes or -1 if
the option is not supported

Method Detail

- isSupportedOption

```java
int isSupportedOption​(
String
option)
```

Determines if the given option is supported and if so, the
number of arguments the option takes.

**Parameters:** option

- an option
**Returns:** the number of arguments the given option takes or -1 if
the option is not supported

---

#### Method Detail

isSupportedOption

```java
int isSupportedOption​(
String
option)
```

Determines if the given option is supported and if so, the
number of arguments the option takes.

**Parameters:** option

- an option
**Returns:** the number of arguments the given option takes or -1 if
the option is not supported

---

#### isSupportedOption

int isSupportedOption​(

String

option)

Determines if the given option is supported and if so, the
number of arguments the option takes.

---

