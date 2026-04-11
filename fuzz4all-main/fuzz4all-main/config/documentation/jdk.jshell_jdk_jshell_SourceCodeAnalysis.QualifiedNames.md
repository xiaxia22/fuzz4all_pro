# Class SourceCodeAnalysis.QualifiedNames

**Source:** `jdk.jshell\jdk\jshell\SourceCodeAnalysis.QualifiedNames.html`

### Class Description

```java
public static final class
SourceCodeAnalysis.QualifiedNames

extends
Object
```

List of possible qualified names.

**Enclosing class:** SourceCodeAnalysis

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public
List
<
String
> getNames()

Known qualified names for the given simple name in the original code.

**Returns:**
- known qualified names

---

#### public int getSimpleNameLength()

The length of the simple name in the original code for which the
qualified names where gathered.

**Returns:**
- the length of the simple name; -1 if there is no name immediately left to the cursor for
which the candidates could be computed

---

#### public boolean isUpToDate()

Indicates whether the result is based on up-to-date data. The

listQualifiedNames

method may return before the classpath is fully inspected, in which case this method will
return

false

. If the result is based on a fully inspected classpath, this method
will return

true

.

**Returns:**
- true

if the result is based on up-to-date data;
otherwise

false

---

#### public boolean isResolvable()

Indicates whether the given simple name in the original code refers
to a resolvable element.

**Returns:**
- true

if the given simple name in the original code
refers to a resolvable element; otherwise

false

---

### Additional Sections

#### Class SourceCodeAnalysis.QualifiedNames

java.lang.Object

- jdk.jshell.SourceCodeAnalysis.QualifiedNames

jdk.jshell.SourceCodeAnalysis.QualifiedNames

**Enclosing class:** SourceCodeAnalysis

```java
public static final class
SourceCodeAnalysis.QualifiedNames

extends
Object
```

List of possible qualified names.

public static final class

SourceCodeAnalysis.QualifiedNames

extends

Object

List of possible qualified names.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

List

<

String

>

getNames

()

Known qualified names for the given simple name in the original code.

int

getSimpleNameLength

()

The length of the simple name in the original code for which the
qualified names where gathered.

boolean

isResolvable

()

Indicates whether the given simple name in the original code refers
to a resolvable element.

boolean

isUpToDate

()

Indicates whether the result is based on up-to-date data.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

List

<

String

>

getNames

()

Known qualified names for the given simple name in the original code.

int

getSimpleNameLength

()

The length of the simple name in the original code for which the
qualified names where gathered.

boolean

isResolvable

()

Indicates whether the given simple name in the original code refers
to a resolvable element.

boolean

isUpToDate

()

Indicates whether the result is based on up-to-date data.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Known qualified names for the given simple name in the original code.

The length of the simple name in the original code for which the
qualified names where gathered.

Indicates whether the given simple name in the original code refers
to a resolvable element.

Indicates whether the result is based on up-to-date data.

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ METHOD DETAIL ==========

- Method Detail

- getNames

```java
public
List
<
String
> getNames()
```

Known qualified names for the given simple name in the original code.

**Returns:** known qualified names

- getSimpleNameLength

```java
public int getSimpleNameLength()
```

The length of the simple name in the original code for which the
qualified names where gathered.

**Returns:** the length of the simple name; -1 if there is no name immediately left to the cursor for
which the candidates could be computed

- isUpToDate

```java
public boolean isUpToDate()
```

Indicates whether the result is based on up-to-date data. The

listQualifiedNames

method may return before the classpath is fully inspected, in which case this method will
return

false

. If the result is based on a fully inspected classpath, this method
will return

true

.

**Returns:** true

if the result is based on up-to-date data;
otherwise

false

- isResolvable

```java
public boolean isResolvable()
```

Indicates whether the given simple name in the original code refers
to a resolvable element.

**Returns:** true

if the given simple name in the original code
refers to a resolvable element; otherwise

false

Method Detail

- getNames

```java
public
List
<
String
> getNames()
```

Known qualified names for the given simple name in the original code.

**Returns:** known qualified names

- getSimpleNameLength

```java
public int getSimpleNameLength()
```

The length of the simple name in the original code for which the
qualified names where gathered.

**Returns:** the length of the simple name; -1 if there is no name immediately left to the cursor for
which the candidates could be computed

- isUpToDate

```java
public boolean isUpToDate()
```

Indicates whether the result is based on up-to-date data. The

listQualifiedNames

method may return before the classpath is fully inspected, in which case this method will
return

false

. If the result is based on a fully inspected classpath, this method
will return

true

.

**Returns:** true

if the result is based on up-to-date data;
otherwise

false

- isResolvable

```java
public boolean isResolvable()
```

Indicates whether the given simple name in the original code refers
to a resolvable element.

**Returns:** true

if the given simple name in the original code
refers to a resolvable element; otherwise

false

---

#### Method Detail

getNames

```java
public
List
<
String
> getNames()
```

Known qualified names for the given simple name in the original code.

**Returns:** known qualified names

---

#### getNames

public

List

<

String

> getNames()

Known qualified names for the given simple name in the original code.

getSimpleNameLength

```java
public int getSimpleNameLength()
```

The length of the simple name in the original code for which the
qualified names where gathered.

**Returns:** the length of the simple name; -1 if there is no name immediately left to the cursor for
which the candidates could be computed

---

#### getSimpleNameLength

public int getSimpleNameLength()

The length of the simple name in the original code for which the
qualified names where gathered.

isUpToDate

```java
public boolean isUpToDate()
```

Indicates whether the result is based on up-to-date data. The

listQualifiedNames

method may return before the classpath is fully inspected, in which case this method will
return

false

. If the result is based on a fully inspected classpath, this method
will return

true

.

**Returns:** true

if the result is based on up-to-date data;
otherwise

false

---

#### isUpToDate

public boolean isUpToDate()

Indicates whether the result is based on up-to-date data. The

listQualifiedNames

method may return before the classpath is fully inspected, in which case this method will
return

false

. If the result is based on a fully inspected classpath, this method
will return

true

.

isResolvable

```java
public boolean isResolvable()
```

Indicates whether the given simple name in the original code refers
to a resolvable element.

**Returns:** true

if the given simple name in the original code
refers to a resolvable element; otherwise

false

---

#### isResolvable

public boolean isResolvable()

Indicates whether the given simple name in the original code refers
to a resolvable element.

---

