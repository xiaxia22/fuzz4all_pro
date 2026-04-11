# Interface NameParser

**Source:** `java.naming\javax\naming\NameParser.html`

### Class Description

```java
public interface
NameParser
```

This interface is used for parsing names from a hierarchical
namespace. The NameParser contains knowledge of the syntactic
information (like left-to-right orientation, name separator, etc.)
needed to parse names.

The equals() method, when used to compare two NameParsers, returns
true if and only if they serve the same namespace.

**Since:** 1.3
**See Also:** CompoundName

,

Name

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Name
parse​(
String
name)
throws
NamingException

Parses a name into its components.

**Parameters:**
- name

- The non-null string name to parse.

**Returns:**
- A non-null parsed form of the name using the naming convention
of this parser.

**Throws:**
- InvalidNameException

- If name does not conform to
syntax defined for the namespace.
- NamingException

- If a naming exception was encountered.

---

### Additional Sections

#### Interface NameParser

```java
public interface
NameParser
```

This interface is used for parsing names from a hierarchical
namespace. The NameParser contains knowledge of the syntactic
information (like left-to-right orientation, name separator, etc.)
needed to parse names.

The equals() method, when used to compare two NameParsers, returns
true if and only if they serve the same namespace.

**Since:** 1.3
**See Also:** CompoundName

,

Name

public interface

NameParser

This interface is used for parsing names from a hierarchical
namespace. The NameParser contains knowledge of the syntactic
information (like left-to-right orientation, name separator, etc.)
needed to parse names.

The equals() method, when used to compare two NameParsers, returns
true if and only if they serve the same namespace.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Name

parse

​(

String

name)

Parses a name into its components.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Name

parse

​(

String

name)

Parses a name into its components.

---

#### Method Summary

Parses a name into its components.

============ METHOD DETAIL ==========

- Method Detail

- parse

```java
Name
parse​(
String
name)
throws
NamingException
```

Parses a name into its components.

**Parameters:** name

- The non-null string name to parse.
**Returns:** A non-null parsed form of the name using the naming convention
of this parser.
**Throws:** InvalidNameException

- If name does not conform to
syntax defined for the namespace.
**Throws:** NamingException

- If a naming exception was encountered.

Method Detail

- parse

```java
Name
parse​(
String
name)
throws
NamingException
```

Parses a name into its components.

**Parameters:** name

- The non-null string name to parse.
**Returns:** A non-null parsed form of the name using the naming convention
of this parser.
**Throws:** InvalidNameException

- If name does not conform to
syntax defined for the namespace.
**Throws:** NamingException

- If a naming exception was encountered.

---

#### Method Detail

parse

```java
Name
parse​(
String
name)
throws
NamingException
```

Parses a name into its components.

**Parameters:** name

- The non-null string name to parse.
**Returns:** A non-null parsed form of the name using the naming convention
of this parser.
**Throws:** InvalidNameException

- If name does not conform to
syntax defined for the namespace.
**Throws:** NamingException

- If a naming exception was encountered.

---

#### parse

Name

parse​(

String

name)
throws

NamingException

Parses a name into its components.

---

