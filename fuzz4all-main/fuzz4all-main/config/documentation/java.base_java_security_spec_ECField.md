# Interface ECField

**Source:** `java.base\java\security\spec\ECField.html`

### Class Description

```java
public interface
ECField
```

This interface represents an elliptic curve (EC) finite field.
All specialized EC fields must implements this interface.

**All Known Implementing Classes:** ECFieldF2m

,

ECFieldFp

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### int getFieldSize()

Returns the field size in bits. Note: For prime finite
field ECFieldFp, size of prime p in bits is returned.
For characteristic 2 finite field ECFieldF2m, m is returned.

**Returns:**
- the field size in bits.

---

### Additional Sections

#### Interface ECField

**All Known Implementing Classes:** ECFieldF2m

,

ECFieldFp

```java
public interface
ECField
```

This interface represents an elliptic curve (EC) finite field.
All specialized EC fields must implements this interface.

**Since:** 1.5
**See Also:** ECFieldFp

,

ECFieldF2m

public interface

ECField

This interface represents an elliptic curve (EC) finite field.
All specialized EC fields must implements this interface.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

getFieldSize

()

Returns the field size in bits.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

getFieldSize

()

Returns the field size in bits.

---

#### Method Summary

Returns the field size in bits.

============ METHOD DETAIL ==========

- Method Detail

- getFieldSize

```java
int getFieldSize()
```

Returns the field size in bits. Note: For prime finite
field ECFieldFp, size of prime p in bits is returned.
For characteristic 2 finite field ECFieldF2m, m is returned.

**Returns:** the field size in bits.

Method Detail

- getFieldSize

```java
int getFieldSize()
```

Returns the field size in bits. Note: For prime finite
field ECFieldFp, size of prime p in bits is returned.
For characteristic 2 finite field ECFieldF2m, m is returned.

**Returns:** the field size in bits.

---

#### Method Detail

getFieldSize

```java
int getFieldSize()
```

Returns the field size in bits. Note: For prime finite
field ECFieldFp, size of prime p in bits is returned.
For characteristic 2 finite field ECFieldF2m, m is returned.

**Returns:** the field size in bits.

---

#### getFieldSize

int getFieldSize()

Returns the field size in bits. Note: For prime finite
field ECFieldFp, size of prime p in bits is returned.
For characteristic 2 finite field ECFieldF2m, m is returned.

---

