# Interface KeySelectorResult

**Source:** `java.xml.crypto\javax\xml\crypto\KeySelectorResult.html`

### Class Description

```java
public interface
KeySelectorResult
```

The result returned by the

KeySelector.select

method.

At a minimum, a

KeySelectorResult

contains the

Key

selected by the

KeySelector

. Implementations of this interface
may add methods to return implementation or algorithm specific information,
such as a chain of certificates or debugging information.

**Since:** 1.6
**See Also:** KeySelector

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Key
getKey()

Returns the selected key.

**Returns:**
- the selected key, or

null

if none can be found

---

### Additional Sections

#### Interface KeySelectorResult

```java
public interface
KeySelectorResult
```

The result returned by the

KeySelector.select

method.

At a minimum, a

KeySelectorResult

contains the

Key

selected by the

KeySelector

. Implementations of this interface
may add methods to return implementation or algorithm specific information,
such as a chain of certificates or debugging information.

**Since:** 1.6
**See Also:** KeySelector

public interface

KeySelectorResult

The result returned by the

KeySelector.select

method.

At a minimum, a

KeySelectorResult

contains the

Key

selected by the

KeySelector

. Implementations of this interface
may add methods to return implementation or algorithm specific information,
such as a chain of certificates or debugging information.

At a minimum, a

KeySelectorResult

contains the

Key

selected by the

KeySelector

. Implementations of this interface
may add methods to return implementation or algorithm specific information,
such as a chain of certificates or debugging information.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Key

getKey

()

Returns the selected key.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Key

getKey

()

Returns the selected key.

---

#### Method Summary

Returns the selected key.

============ METHOD DETAIL ==========

- Method Detail

- getKey

```java
Key
getKey()
```

Returns the selected key.

**Returns:** the selected key, or

null

if none can be found

Method Detail

- getKey

```java
Key
getKey()
```

Returns the selected key.

**Returns:** the selected key, or

null

if none can be found

---

#### Method Detail

getKey

```java
Key
getKey()
```

Returns the selected key.

**Returns:** the selected key, or

null

if none can be found

---

#### getKey

Key

getKey()

Returns the selected key.

---

