# Interface SourceCodeAnalysis.Suggestion

**Source:** `jdk.jshell\jdk\jshell\SourceCodeAnalysis.Suggestion.html`

### Class Description

```java
public static interface
SourceCodeAnalysis.Suggestion
```

A candidate for continuation of the given user's input.

**Enclosing class:** SourceCodeAnalysis

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
continuation()

The candidate continuation of the given user's input.

**Returns:**
- the continuation string

---

#### boolean matchesType()

Indicates whether input continuation matches the target type and is thus
more likely to be the desired continuation. A matching continuation is
preferred.

**Returns:**
- true

if this suggested continuation matches the
target type; otherwise

false

---

### Additional Sections

#### Interface SourceCodeAnalysis.Suggestion

**Enclosing class:** SourceCodeAnalysis

```java
public static interface
SourceCodeAnalysis.Suggestion
```

A candidate for continuation of the given user's input.

public static interface

SourceCodeAnalysis.Suggestion

A candidate for continuation of the given user's input.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

continuation

()

The candidate continuation of the given user's input.

boolean

matchesType

()

Indicates whether input continuation matches the target type and is thus
more likely to be the desired continuation.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

continuation

()

The candidate continuation of the given user's input.

boolean

matchesType

()

Indicates whether input continuation matches the target type and is thus
more likely to be the desired continuation.

---

#### Method Summary

The candidate continuation of the given user's input.

Indicates whether input continuation matches the target type and is thus
more likely to be the desired continuation.

============ METHOD DETAIL ==========

- Method Detail

- continuation

```java
String
continuation()
```

The candidate continuation of the given user's input.

**Returns:** the continuation string

- matchesType

```java
boolean matchesType()
```

Indicates whether input continuation matches the target type and is thus
more likely to be the desired continuation. A matching continuation is
preferred.

**Returns:** true

if this suggested continuation matches the
target type; otherwise

false

Method Detail

- continuation

```java
String
continuation()
```

The candidate continuation of the given user's input.

**Returns:** the continuation string

- matchesType

```java
boolean matchesType()
```

Indicates whether input continuation matches the target type and is thus
more likely to be the desired continuation. A matching continuation is
preferred.

**Returns:** true

if this suggested continuation matches the
target type; otherwise

false

---

#### Method Detail

continuation

```java
String
continuation()
```

The candidate continuation of the given user's input.

**Returns:** the continuation string

---

#### continuation

String

continuation()

The candidate continuation of the given user's input.

matchesType

```java
boolean matchesType()
```

Indicates whether input continuation matches the target type and is thus
more likely to be the desired continuation. A matching continuation is
preferred.

**Returns:** true

if this suggested continuation matches the
target type; otherwise

false

---

#### matchesType

boolean matchesType()

Indicates whether input continuation matches the target type and is thus
more likely to be the desired continuation. A matching continuation is
preferred.

---

