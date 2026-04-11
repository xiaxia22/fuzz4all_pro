# Interface ClassFilter

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\scripting\ClassFilter.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
ClassFilter
```

Class filter (optional) to be used by nashorn script engine.
jsr-223 program embedding nashorn script can set ClassFilter instance
to be used when an engine instance is created.

**Since:** 1.8u40

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean exposeToScripts​(
String
className)

Should the Java class of the specified name be exposed to scripts?

**Parameters:**
- className

- is the fully qualified name of the java class being
checked. This will not be null. Only non-array class names will be
passed.

**Returns:**
- true if the java class can be exposed to scripts false otherwise

---

### Additional Sections

#### Interface ClassFilter

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
ClassFilter
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

Class filter (optional) to be used by nashorn script engine.
jsr-223 program embedding nashorn script can set ClassFilter instance
to be used when an engine instance is created.

**Since:** 1.8u40

@Deprecated

(

since

="11",

forRemoval

=true)
public interface

ClassFilter

Class filter (optional) to be used by nashorn script engine.
jsr-223 program embedding nashorn script can set ClassFilter instance
to be used when an engine instance is created.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

boolean

exposeToScripts

​(

String

className)

Deprecated, for removal: This API element is subject to removal in a future version.

Should the Java class of the specified name be exposed to scripts?

Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

boolean

exposeToScripts

​(

String

className)

Deprecated, for removal: This API element is subject to removal in a future version.

Should the Java class of the specified name be exposed to scripts?

---

#### Method Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Should the Java class of the specified name be exposed to scripts?

============ METHOD DETAIL ==========

- Method Detail

- exposeToScripts

```java
boolean exposeToScripts​(
String
className)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Should the Java class of the specified name be exposed to scripts?

**Parameters:** className

- is the fully qualified name of the java class being
checked. This will not be null. Only non-array class names will be
passed.
**Returns:** true if the java class can be exposed to scripts false otherwise

Method Detail

- exposeToScripts

```java
boolean exposeToScripts​(
String
className)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Should the Java class of the specified name be exposed to scripts?

**Parameters:** className

- is the fully qualified name of the java class being
checked. This will not be null. Only non-array class names will be
passed.
**Returns:** true if the java class can be exposed to scripts false otherwise

---

#### Method Detail

exposeToScripts

```java
boolean exposeToScripts​(
String
className)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Should the Java class of the specified name be exposed to scripts?

**Parameters:** className

- is the fully qualified name of the java class being
checked. This will not be null. Only non-array class names will be
passed.
**Returns:** true if the java class can be exposed to scripts false otherwise

---

#### exposeToScripts

boolean exposeToScripts​(

String

className)

Should the Java class of the specified name be exposed to scripts?

---

