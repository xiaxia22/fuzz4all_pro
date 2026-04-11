# Interface SQLType

**Source:** `java.sql\java\sql\SQLType.html`

### Class Description

```java
public interface
SQLType
```

An object that is used to identify a generic SQL type, called a JDBC type or
a vendor specific data type.

**All Known Implementing Classes:** JDBCType

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getName()

Returns the

SQLType

name that represents a SQL data type.

**Returns:**
- The name of this

SQLType

.

---

#### String
getVendor()

Returns the name of the vendor that supports this data type. The value
returned typically is the package name for this vendor.

**Returns:**
- The name of the vendor for this data type

---

#### Integer
getVendorTypeNumber()

Returns the vendor specific type number for the data type.

**Returns:**
- An Integer representing the vendor specific data type

---

### Additional Sections

#### Interface SQLType

**All Known Implementing Classes:** JDBCType

```java
public interface
SQLType
```

An object that is used to identify a generic SQL type, called a JDBC type or
a vendor specific data type.

**Since:** 1.8

public interface

SQLType

An object that is used to identify a generic SQL type, called a JDBC type or
a vendor specific data type.

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

Returns the

SQLType

name that represents a SQL data type.

String

getVendor

()

Returns the name of the vendor that supports this data type.

Integer

getVendorTypeNumber

()

Returns the vendor specific type number for the data type.

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

Returns the

SQLType

name that represents a SQL data type.

String

getVendor

()

Returns the name of the vendor that supports this data type.

Integer

getVendorTypeNumber

()

Returns the vendor specific type number for the data type.

---

#### Method Summary

Returns the

SQLType

name that represents a SQL data type.

Returns the name of the vendor that supports this data type.

Returns the vendor specific type number for the data type.

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
String
getName()
```

Returns the

SQLType

name that represents a SQL data type.

**Returns:** The name of this

SQLType

.

- getVendor

```java
String
getVendor()
```

Returns the name of the vendor that supports this data type. The value
returned typically is the package name for this vendor.

**Returns:** The name of the vendor for this data type

- getVendorTypeNumber

```java
Integer
getVendorTypeNumber()
```

Returns the vendor specific type number for the data type.

**Returns:** An Integer representing the vendor specific data type

Method Detail

- getName

```java
String
getName()
```

Returns the

SQLType

name that represents a SQL data type.

**Returns:** The name of this

SQLType

.

- getVendor

```java
String
getVendor()
```

Returns the name of the vendor that supports this data type. The value
returned typically is the package name for this vendor.

**Returns:** The name of the vendor for this data type

- getVendorTypeNumber

```java
Integer
getVendorTypeNumber()
```

Returns the vendor specific type number for the data type.

**Returns:** An Integer representing the vendor specific data type

---

#### Method Detail

getName

```java
String
getName()
```

Returns the

SQLType

name that represents a SQL data type.

**Returns:** The name of this

SQLType

.

---

#### getName

String

getName()

Returns the

SQLType

name that represents a SQL data type.

getVendor

```java
String
getVendor()
```

Returns the name of the vendor that supports this data type. The value
returned typically is the package name for this vendor.

**Returns:** The name of the vendor for this data type

---

#### getVendor

String

getVendor()

Returns the name of the vendor that supports this data type. The value
returned typically is the package name for this vendor.

getVendorTypeNumber

```java
Integer
getVendorTypeNumber()
```

Returns the vendor specific type number for the data type.

**Returns:** An Integer representing the vendor specific data type

---

#### getVendorTypeNumber

Integer

getVendorTypeNumber()

Returns the vendor specific type number for the data type.

---

