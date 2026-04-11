# Interface URIException

**Source:** `java.desktop\javax\print\URIException.html`

### Class Description

```java
public interface
URIException
```

Interface

URIException

is a mixin interface which a subclass of

PrintException

can implement to report an error
condition involving a

URI

address. The Print Service API does not
define any print exception classes that implement interface

URIException

, that being left to the Print Service implementor's
discretion.

---

### Field Details

#### static final int URIInaccessible

Indicates that the printer cannot access the

URI

address. For
example, the printer might report this error if it goes to get the print
data and cannot even establish a connection to the

URI

address.

**See Also:**
- Constant Field Values

---

#### static final int URISchemeNotSupported

Indicates that the printer does not support the

URI

scheme
("http", "ftp", etc.) in the

URI

address.

**See Also:**
- Constant Field Values

---

#### static final int URIOtherProblem

Indicates any kind of problem not specifically identified by the other
reasons.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### URI
getUnsupportedURI()

Returns the

URI

.

**Returns:**
- the

URI

that is the cause of this exception

---

#### int getReason()

Returns the reason of this exception.

**Returns:**
- one of the predefined reasons enumerated in this interface

---

### Additional Sections

#### Interface URIException

```java
public interface
URIException
```

Interface

URIException

is a mixin interface which a subclass of

PrintException

can implement to report an error
condition involving a

URI

address. The Print Service API does not
define any print exception classes that implement interface

URIException

, that being left to the Print Service implementor's
discretion.

public interface

URIException

Interface

URIException

is a mixin interface which a subclass of

PrintException

can implement to report an error
condition involving a

URI

address. The Print Service API does not
define any print exception classes that implement interface

URIException

, that being left to the Print Service implementor's
discretion.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

URIInaccessible

Indicates that the printer cannot access the

URI

address.

static int

URIOtherProblem

Indicates any kind of problem not specifically identified by the other
reasons.

static int

URISchemeNotSupported

Indicates that the printer does not support the

URI

scheme
("http", "ftp", etc.) in the

URI

address.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

getReason

()

Returns the reason of this exception.

URI

getUnsupportedURI

()

Returns the

URI

.

Field Summary

Fields

Modifier and Type

Field

Description

static int

URIInaccessible

Indicates that the printer cannot access the

URI

address.

static int

URIOtherProblem

Indicates any kind of problem not specifically identified by the other
reasons.

static int

URISchemeNotSupported

Indicates that the printer does not support the

URI

scheme
("http", "ftp", etc.) in the

URI

address.

---

#### Field Summary

Indicates that the printer cannot access the

URI

address.

Indicates any kind of problem not specifically identified by the other
reasons.

Indicates that the printer does not support the

URI

scheme
("http", "ftp", etc.) in the

URI

address.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

getReason

()

Returns the reason of this exception.

URI

getUnsupportedURI

()

Returns the

URI

.

---

#### Method Summary

Returns the reason of this exception.

Returns the

URI

.

============ FIELD DETAIL ===========

- Field Detail

- URIInaccessible

```java
static final int URIInaccessible
```

Indicates that the printer cannot access the

URI

address. For
example, the printer might report this error if it goes to get the print
data and cannot even establish a connection to the

URI

address.

**See Also:** Constant Field Values

- URISchemeNotSupported

```java
static final int URISchemeNotSupported
```

Indicates that the printer does not support the

URI

scheme
("http", "ftp", etc.) in the

URI

address.

**See Also:** Constant Field Values

- URIOtherProblem

```java
static final int URIOtherProblem
```

Indicates any kind of problem not specifically identified by the other
reasons.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getUnsupportedURI

```java
URI
getUnsupportedURI()
```

Returns the

URI

.

**Returns:** the

URI

that is the cause of this exception

- getReason

```java
int getReason()
```

Returns the reason of this exception.

**Returns:** one of the predefined reasons enumerated in this interface

Field Detail

- URIInaccessible

```java
static final int URIInaccessible
```

Indicates that the printer cannot access the

URI

address. For
example, the printer might report this error if it goes to get the print
data and cannot even establish a connection to the

URI

address.

**See Also:** Constant Field Values

- URISchemeNotSupported

```java
static final int URISchemeNotSupported
```

Indicates that the printer does not support the

URI

scheme
("http", "ftp", etc.) in the

URI

address.

**See Also:** Constant Field Values

- URIOtherProblem

```java
static final int URIOtherProblem
```

Indicates any kind of problem not specifically identified by the other
reasons.

**See Also:** Constant Field Values

---

#### Field Detail

URIInaccessible

```java
static final int URIInaccessible
```

Indicates that the printer cannot access the

URI

address. For
example, the printer might report this error if it goes to get the print
data and cannot even establish a connection to the

URI

address.

**See Also:** Constant Field Values

---

#### URIInaccessible

static final int URIInaccessible

Indicates that the printer cannot access the

URI

address. For
example, the printer might report this error if it goes to get the print
data and cannot even establish a connection to the

URI

address.

URISchemeNotSupported

```java
static final int URISchemeNotSupported
```

Indicates that the printer does not support the

URI

scheme
("http", "ftp", etc.) in the

URI

address.

**See Also:** Constant Field Values

---

#### URISchemeNotSupported

static final int URISchemeNotSupported

Indicates that the printer does not support the

URI

scheme
("http", "ftp", etc.) in the

URI

address.

URIOtherProblem

```java
static final int URIOtherProblem
```

Indicates any kind of problem not specifically identified by the other
reasons.

**See Also:** Constant Field Values

---

#### URIOtherProblem

static final int URIOtherProblem

Indicates any kind of problem not specifically identified by the other
reasons.

Method Detail

- getUnsupportedURI

```java
URI
getUnsupportedURI()
```

Returns the

URI

.

**Returns:** the

URI

that is the cause of this exception

- getReason

```java
int getReason()
```

Returns the reason of this exception.

**Returns:** one of the predefined reasons enumerated in this interface

---

#### Method Detail

getUnsupportedURI

```java
URI
getUnsupportedURI()
```

Returns the

URI

.

**Returns:** the

URI

that is the cause of this exception

---

#### getUnsupportedURI

URI

getUnsupportedURI()

Returns the

URI

.

getReason

```java
int getReason()
```

Returns the reason of this exception.

**Returns:** one of the predefined reasons enumerated in this interface

---

#### getReason

int getReason()

Returns the reason of this exception.

---

