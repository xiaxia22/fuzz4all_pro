# Interface ObjectInputValidation

**Source:** `java.base\java\io\ObjectInputValidation.html`

### Class Description

```java
public interface
ObjectInputValidation
```

Callback interface to allow validation of objects within a graph.
Allows an object to be called when a complete graph of objects has
been deserialized.

**Since:** 1.1
**See Also:** ObjectInputStream

,

ObjectInputStream.registerValidation(java.io.ObjectInputValidation, int)

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void validateObject()
throws
InvalidObjectException

Validates the object.

**Throws:**
- InvalidObjectException

- If the object cannot validate itself.

---

### Additional Sections

#### Interface ObjectInputValidation

```java
public interface
ObjectInputValidation
```

Callback interface to allow validation of objects within a graph.
Allows an object to be called when a complete graph of objects has
been deserialized.

**Since:** 1.1
**See Also:** ObjectInputStream

,

ObjectInputStream.registerValidation(java.io.ObjectInputValidation, int)

public interface

ObjectInputValidation

Callback interface to allow validation of objects within a graph.
Allows an object to be called when a complete graph of objects has
been deserialized.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

validateObject

()

Validates the object.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

validateObject

()

Validates the object.

---

#### Method Summary

Validates the object.

============ METHOD DETAIL ==========

- Method Detail

- validateObject

```java
void validateObject()
throws
InvalidObjectException
```

Validates the object.

**Throws:** InvalidObjectException

- If the object cannot validate itself.

Method Detail

- validateObject

```java
void validateObject()
throws
InvalidObjectException
```

Validates the object.

**Throws:** InvalidObjectException

- If the object cannot validate itself.

---

#### Method Detail

validateObject

```java
void validateObject()
throws
InvalidObjectException
```

Validates the object.

**Throws:** InvalidObjectException

- If the object cannot validate itself.

---

#### validateObject

void validateObject()
throws

InvalidObjectException

Validates the object.

---

