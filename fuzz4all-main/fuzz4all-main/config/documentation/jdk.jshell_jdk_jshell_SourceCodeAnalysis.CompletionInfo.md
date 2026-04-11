# Interface SourceCodeAnalysis.CompletionInfo

**Source:** `jdk.jshell\jdk\jshell\SourceCodeAnalysis.CompletionInfo.html`

### Class Description

```java
public static interface
SourceCodeAnalysis.CompletionInfo
```

The result of

analyzeCompletion(String input)

.
Describes the completeness of the first snippet in the given input.

**Enclosing class:** SourceCodeAnalysis

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### SourceCodeAnalysis.Completeness
completeness()

The analyzed completeness of the input.

**Returns:**
- an enum describing the completeness of the input string.

---

#### String
remaining()

Input remaining after the complete part of the source.

**Returns:**
- the portion of the input string that remains after the
complete Snippet

---

#### String
source()

Source code for the first Snippet of code input. For example, first
statement, or first method declaration. Trailing semicolons will be
added, as needed.

**Returns:**
- the source of the first encountered Snippet

---

### Additional Sections

#### Interface SourceCodeAnalysis.CompletionInfo

**Enclosing class:** SourceCodeAnalysis

```java
public static interface
SourceCodeAnalysis.CompletionInfo
```

The result of

analyzeCompletion(String input)

.
Describes the completeness of the first snippet in the given input.

public static interface

SourceCodeAnalysis.CompletionInfo

The result of

analyzeCompletion(String input)

.
Describes the completeness of the first snippet in the given input.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

SourceCodeAnalysis.Completeness

completeness

()

The analyzed completeness of the input.

String

remaining

()

Input remaining after the complete part of the source.

String

source

()

Source code for the first Snippet of code input.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

SourceCodeAnalysis.Completeness

completeness

()

The analyzed completeness of the input.

String

remaining

()

Input remaining after the complete part of the source.

String

source

()

Source code for the first Snippet of code input.

---

#### Method Summary

The analyzed completeness of the input.

Input remaining after the complete part of the source.

Source code for the first Snippet of code input.

============ METHOD DETAIL ==========

- Method Detail

- completeness

```java
SourceCodeAnalysis.Completeness
completeness()
```

The analyzed completeness of the input.

**Returns:** an enum describing the completeness of the input string.

- remaining

```java
String
remaining()
```

Input remaining after the complete part of the source.

**Returns:** the portion of the input string that remains after the
complete Snippet

- source

```java
String
source()
```

Source code for the first Snippet of code input. For example, first
statement, or first method declaration. Trailing semicolons will be
added, as needed.

**Returns:** the source of the first encountered Snippet

Method Detail

- completeness

```java
SourceCodeAnalysis.Completeness
completeness()
```

The analyzed completeness of the input.

**Returns:** an enum describing the completeness of the input string.

- remaining

```java
String
remaining()
```

Input remaining after the complete part of the source.

**Returns:** the portion of the input string that remains after the
complete Snippet

- source

```java
String
source()
```

Source code for the first Snippet of code input. For example, first
statement, or first method declaration. Trailing semicolons will be
added, as needed.

**Returns:** the source of the first encountered Snippet

---

#### Method Detail

completeness

```java
SourceCodeAnalysis.Completeness
completeness()
```

The analyzed completeness of the input.

**Returns:** an enum describing the completeness of the input string.

---

#### completeness

SourceCodeAnalysis.Completeness

completeness()

The analyzed completeness of the input.

remaining

```java
String
remaining()
```

Input remaining after the complete part of the source.

**Returns:** the portion of the input string that remains after the
complete Snippet

---

#### remaining

String

remaining()

Input remaining after the complete part of the source.

source

```java
String
source()
```

Source code for the first Snippet of code input. For example, first
statement, or first method declaration. Trailing semicolons will be
added, as needed.

**Returns:** the source of the first encountered Snippet

---

#### source

String

source()

Source code for the first Snippet of code input. For example, first
statement, or first method declaration. Trailing semicolons will be
added, as needed.

---

