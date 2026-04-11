# Interface KeyStore.Entry.Attribute

**Source:** `java.base\java\security\KeyStore.Entry.Attribute.html`

### Class Description

```java
public static interface
KeyStore.Entry.Attribute
```

An attribute associated with a keystore entry.
It comprises a name and one or more values.

**All Known Implementing Classes:** PKCS12Attribute

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getName()

Returns the attribute's name.

**Returns:**
- the attribute name

---

#### String
getValue()

Returns the attribute's value.
Multi-valued attributes encode their values as a single string.

**Returns:**
- the attribute value

---

### Additional Sections

#### Interface KeyStore.Entry.Attribute

**All Known Implementing Classes:** PKCS12Attribute

**Enclosing interface:** KeyStore.Entry

```java
public static interface
KeyStore.Entry.Attribute
```

An attribute associated with a keystore entry.
It comprises a name and one or more values.

**Since:** 1.8

public static interface

KeyStore.Entry.Attribute

An attribute associated with a keystore entry.
It comprises a name and one or more values.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getName

()

Returns the attribute's name.

String

getValue

()

Returns the attribute's value.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getName

()

Returns the attribute's name.

String

getValue

()

Returns the attribute's value.

---

#### Method Summary

Returns the attribute's name.

Returns the attribute's value.

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
String
getName()
```

Returns the attribute's name.

**Returns:** the attribute name

- getValue

```java
String
getValue()
```

Returns the attribute's value.
Multi-valued attributes encode their values as a single string.

**Returns:** the attribute value

Method Detail

- getName

```java
String
getName()
```

Returns the attribute's name.

**Returns:** the attribute name

- getValue

```java
String
getValue()
```

Returns the attribute's value.
Multi-valued attributes encode their values as a single string.

**Returns:** the attribute value

---

#### Method Detail

getName

```java
String
getName()
```

Returns the attribute's name.

**Returns:** the attribute name

---

#### getName

String

getName()

Returns the attribute's name.

getValue

```java
String
getValue()
```

Returns the attribute's value.
Multi-valued attributes encode their values as a single string.

**Returns:** the attribute value

---

#### getValue

String

getValue()

Returns the attribute's value.
Multi-valued attributes encode their values as a single string.

---

