# Interface FlavorException

**Source:** `java.desktop\javax\print\FlavorException.html`

### Class Description

```java
public interface
FlavorException
```

Interface

FlavorException

is a mixin interface which a subclass of

PrintException

can implement to report an error
condition involving a doc flavor or flavors (class

DocFlavor

). The
Print Service API does not define any print exception classes that implement
interface

FlavorException

, that being left to the Print Service
implementor's discretion.

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### DocFlavor
[] getUnsupportedFlavors()

Returns the unsupported flavors.

**Returns:**
- the unsupported doc flavors

---

### Additional Sections

#### Interface FlavorException

```java
public interface
FlavorException
```

Interface

FlavorException

is a mixin interface which a subclass of

PrintException

can implement to report an error
condition involving a doc flavor or flavors (class

DocFlavor

). The
Print Service API does not define any print exception classes that implement
interface

FlavorException

, that being left to the Print Service
implementor's discretion.

public interface

FlavorException

Interface

FlavorException

is a mixin interface which a subclass of

PrintException

can implement to report an error
condition involving a doc flavor or flavors (class

DocFlavor

). The
Print Service API does not define any print exception classes that implement
interface

FlavorException

, that being left to the Print Service
implementor's discretion.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

DocFlavor

[]

getUnsupportedFlavors

()

Returns the unsupported flavors.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

DocFlavor

[]

getUnsupportedFlavors

()

Returns the unsupported flavors.

---

#### Method Summary

Returns the unsupported flavors.

============ METHOD DETAIL ==========

- Method Detail

- getUnsupportedFlavors

```java
DocFlavor
[] getUnsupportedFlavors()
```

Returns the unsupported flavors.

**Returns:** the unsupported doc flavors

Method Detail

- getUnsupportedFlavors

```java
DocFlavor
[] getUnsupportedFlavors()
```

Returns the unsupported flavors.

**Returns:** the unsupported doc flavors

---

#### Method Detail

getUnsupportedFlavors

```java
DocFlavor
[] getUnsupportedFlavors()
```

Returns the unsupported flavors.

**Returns:** the unsupported doc flavors

---

#### getUnsupportedFlavors

DocFlavor

[] getUnsupportedFlavors()

Returns the unsupported flavors.

---

