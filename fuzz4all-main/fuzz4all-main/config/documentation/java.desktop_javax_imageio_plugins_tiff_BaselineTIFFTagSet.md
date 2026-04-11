# Class BaselineTIFFTagSet

**Source:** `java.desktop\javax\imageio\plugins\tiff\BaselineTIFFTagSet.html`

### Class Description

```java
public final class
BaselineTIFFTagSet

extends
TIFFTagSet
```

A class representing the set of tags found in the baseline TIFF
specification as well as some common additional tags.

The non-baseline tags included in this class are:

- JPEGTables

ICC Profile

The non-baseline values of baseline tags included in this class are

- Compression

tag values:

- JPEG-in-TIFF compression
- Zlib-in-TIFF compression
- Deflate compression
- PhotometricInterpretation

tag values:

- ICCLAB
photometric interpretation

**Since:** 9
**See Also:** TIFF 6.0 Specification

---

### Field Details

#### public static final int TAG_NEW_SUBFILE_TYPE

Constant specifying the "NewSubfileType" tag.

**See Also:**
- NEW_SUBFILE_TYPE_REDUCED_RESOLUTION

,

NEW_SUBFILE_TYPE_SINGLE_PAGE

,

NEW_SUBFILE_TYPE_TRANSPARENCY

,

Constant Field Values

---

#### public static final int NEW_SUBFILE_TYPE_REDUCED_RESOLUTION

A mask to be used with the "NewSubfileType" tag.

**See Also:**
- TAG_NEW_SUBFILE_TYPE

,

Constant Field Values

---

#### public static final int NEW_SUBFILE_TYPE_SINGLE_PAGE

A mask to be used with the "NewSubfileType" tag.

**See Also:**
- TAG_NEW_SUBFILE_TYPE

,

Constant Field Values

---

#### public static final int NEW_SUBFILE_TYPE_TRANSPARENCY

A mask to be used with the "NewSubfileType" tag.

**See Also:**
- TAG_NEW_SUBFILE_TYPE

,

Constant Field Values

---

#### public static final int TAG_SUBFILE_TYPE

Constant specifying the "SubfileType" tag.

**See Also:**
- SUBFILE_TYPE_FULL_RESOLUTION

,

SUBFILE_TYPE_REDUCED_RESOLUTION

,

SUBFILE_TYPE_SINGLE_PAGE

,

Constant Field Values

---

#### public static final int SUBFILE_TYPE_FULL_RESOLUTION

A value to be used with the "SubfileType" tag.

**See Also:**
- TAG_SUBFILE_TYPE

,

Constant Field Values

---

#### public static final int SUBFILE_TYPE_REDUCED_RESOLUTION

A value to be used with the "SubfileType" tag.

**See Also:**
- TAG_SUBFILE_TYPE

,

Constant Field Values

---

#### public static final int SUBFILE_TYPE_SINGLE_PAGE

A value to be used with the "SubfileType" tag.

**See Also:**
- TAG_SUBFILE_TYPE

,

Constant Field Values

---

#### public static final int TAG_IMAGE_WIDTH

Constant specifying the "ImageWidth" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_IMAGE_LENGTH

Constant specifying the "ImageLength" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_BITS_PER_SAMPLE

Constant specifying the "BitsPerSample" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_COMPRESSION

Constant specifying the "Compression" tag.

**See Also:**
- COMPRESSION_NONE

,

COMPRESSION_CCITT_RLE

,

COMPRESSION_CCITT_T_4

,

COMPRESSION_CCITT_T_6

,

COMPRESSION_LZW

,

COMPRESSION_OLD_JPEG

,

COMPRESSION_JPEG

,

COMPRESSION_ZLIB

,

COMPRESSION_PACKBITS

,

COMPRESSION_DEFLATE

,

Constant Field Values

---

#### public static final int COMPRESSION_NONE

A value to be used with the "Compression" tag.

**See Also:**
- TAG_COMPRESSION

,

Constant Field Values

---

#### public static final int COMPRESSION_CCITT_RLE

A value to be used with the "Compression" tag.

**See Also:**
- TAG_COMPRESSION

,

Constant Field Values

---

#### public static final int COMPRESSION_CCITT_T_4

A value to be used with the "Compression" tag.

**See Also:**
- TAG_COMPRESSION

,

Constant Field Values

---

#### public static final int COMPRESSION_CCITT_T_6

A value to be used with the "Compression" tag.

**See Also:**
- TAG_COMPRESSION

,

Constant Field Values

---

#### public static final int COMPRESSION_LZW

A value to be used with the "Compression" tag.

**See Also:**
- TAG_COMPRESSION

,

Constant Field Values

---

#### public static final int COMPRESSION_OLD_JPEG

A value to be used with the "Compression" tag.

**See Also:**
- TAG_COMPRESSION

,

Constant Field Values

---

#### public static final int COMPRESSION_JPEG

A value to be used with the "Compression" tag.

**See Also:**
- TAG_COMPRESSION

,

Constant Field Values

---

#### public static final int COMPRESSION_ZLIB

A value to be used with the "Compression" tag.

**See Also:**
- TAG_COMPRESSION

,

Constant Field Values

---

#### public static final int COMPRESSION_PACKBITS

A value to be used with the "Compression" tag.

**See Also:**
- TAG_COMPRESSION

,

Constant Field Values

---

#### public static final int COMPRESSION_DEFLATE

A value to be used with the "Compression" tag.

**See Also:**
- TAG_COMPRESSION

,

DEFLATE specification

,

Constant Field Values

---

#### public static final int TAG_PHOTOMETRIC_INTERPRETATION

Constant specifying the "PhotometricInterpretation" tag.

**See Also:**
- PHOTOMETRIC_INTERPRETATION_WHITE_IS_ZERO

,

PHOTOMETRIC_INTERPRETATION_BLACK_IS_ZERO

,

PHOTOMETRIC_INTERPRETATION_RGB

,

PHOTOMETRIC_INTERPRETATION_PALETTE_COLOR

,

PHOTOMETRIC_INTERPRETATION_TRANSPARENCY_MASK

,

PHOTOMETRIC_INTERPRETATION_Y_CB_CR

,

PHOTOMETRIC_INTERPRETATION_CIELAB

,

PHOTOMETRIC_INTERPRETATION_ICCLAB

,

Constant Field Values

---

#### public static final int PHOTOMETRIC_INTERPRETATION_WHITE_IS_ZERO

A value to be used with the "PhotometricInterpretation" tag.

**See Also:**
- TAG_PHOTOMETRIC_INTERPRETATION

,

Constant Field Values

---

#### public static final int PHOTOMETRIC_INTERPRETATION_BLACK_IS_ZERO

A value to be used with the "PhotometricInterpretation" tag.

**See Also:**
- TAG_PHOTOMETRIC_INTERPRETATION

,

Constant Field Values

---

#### public static final int PHOTOMETRIC_INTERPRETATION_RGB

A value to be used with the "PhotometricInterpretation" tag.

**See Also:**
- TAG_PHOTOMETRIC_INTERPRETATION

,

Constant Field Values

---

#### public static final int PHOTOMETRIC_INTERPRETATION_PALETTE_COLOR

A value to be used with the "PhotometricInterpretation" tag.

**See Also:**
- TAG_PHOTOMETRIC_INTERPRETATION

,

Constant Field Values

---

#### public static final int PHOTOMETRIC_INTERPRETATION_TRANSPARENCY_MASK

A value to be used with the "PhotometricInterpretation" tag.

**See Also:**
- TAG_PHOTOMETRIC_INTERPRETATION

,

Constant Field Values

---

#### public static final int PHOTOMETRIC_INTERPRETATION_CMYK

A value to be used with the "PhotometricInterpretation" tag.

**See Also:**
- TAG_PHOTOMETRIC_INTERPRETATION

,

Constant Field Values

---

#### public static final int PHOTOMETRIC_INTERPRETATION_Y_CB_CR

A value to be used with the "PhotometricInterpretation" tag.

**See Also:**
- TAG_PHOTOMETRIC_INTERPRETATION

,

Constant Field Values

---

#### public static final int PHOTOMETRIC_INTERPRETATION_CIELAB

A value to be used with the "PhotometricInterpretation" tag.

**See Also:**
- TAG_PHOTOMETRIC_INTERPRETATION

,

Constant Field Values

---

#### public static final int PHOTOMETRIC_INTERPRETATION_ICCLAB

A value to be used with the "PhotometricInterpretation" tag.

**See Also:**
- TAG_PHOTOMETRIC_INTERPRETATION

,

Constant Field Values

---

#### public static final int TAG_THRESHHOLDING

Constant specifying the "Threshholding" tag.

**See Also:**
- THRESHHOLDING_NONE

,

THRESHHOLDING_ORDERED_DITHER

,

THRESHHOLDING_RANDOMIZED_DITHER

,

Constant Field Values

---

#### public static final int THRESHHOLDING_NONE

A value to be used with the "Thresholding" tag.

**See Also:**
- TAG_THRESHHOLDING

,

Constant Field Values

---

#### public static final int THRESHHOLDING_ORDERED_DITHER

A value to be used with the "Thresholding" tag.

**See Also:**
- TAG_THRESHHOLDING

,

Constant Field Values

---

#### public static final int THRESHHOLDING_RANDOMIZED_DITHER

A value to be used with the "Thresholding" tag.

**See Also:**
- TAG_THRESHHOLDING

,

Constant Field Values

---

#### public static final int TAG_CELL_WIDTH

Constant specifying the "Cell_Width" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_CELL_LENGTH

Constant specifying the "cell_length" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_FILL_ORDER

Constant specifying the "fill_order" tag.

**See Also:**
- FILL_ORDER_LEFT_TO_RIGHT

,

FILL_ORDER_RIGHT_TO_LEFT

,

Constant Field Values

---

#### public static final int FILL_ORDER_LEFT_TO_RIGHT

A value to be used with the "FillOrder" tag.

**See Also:**
- TAG_FILL_ORDER

,

Constant Field Values

---

#### public static final int FILL_ORDER_RIGHT_TO_LEFT

A value to be used with the "FillOrder" tag.

**See Also:**
- TAG_FILL_ORDER

,

Constant Field Values

---

#### public static final int TAG_DOCUMENT_NAME

Constant specifying the "document_name" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_IMAGE_DESCRIPTION

Constant specifying the "Image_description" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_MAKE

Constant specifying the "Make" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_MODEL

Constant specifying the "Model" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_STRIP_OFFSETS

Constant specifying the "Strip_offsets" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_ORIENTATION

Constant specifying the "Orientation" tag.

**See Also:**
- ORIENTATION_ROW_0_TOP_COLUMN_0_LEFT

,

ORIENTATION_ROW_0_TOP_COLUMN_0_RIGHT

,

ORIENTATION_ROW_0_BOTTOM_COLUMN_0_RIGHT

,

ORIENTATION_ROW_0_BOTTOM_COLUMN_0_LEFT

,

ORIENTATION_ROW_0_LEFT_COLUMN_0_TOP

,

ORIENTATION_ROW_0_RIGHT_COLUMN_0_TOP

,

ORIENTATION_ROW_0_RIGHT_COLUMN_0_BOTTOM

,

ORIENTATION_ROW_0_LEFT_COLUMN_0_BOTTOM

,

Constant Field Values

---

#### public static final int ORIENTATION_ROW_0_TOP_COLUMN_0_LEFT

A value to be used with the "Orientation" tag.

**See Also:**
- TAG_ORIENTATION

,

Constant Field Values

---

#### public static final int ORIENTATION_ROW_0_TOP_COLUMN_0_RIGHT

A value to be used with the "Orientation" tag.

**See Also:**
- TAG_ORIENTATION

,

Constant Field Values

---

#### public static final int ORIENTATION_ROW_0_BOTTOM_COLUMN_0_RIGHT

A value to be used with the "Orientation" tag.

**See Also:**
- TAG_ORIENTATION

,

Constant Field Values

---

#### public static final int ORIENTATION_ROW_0_BOTTOM_COLUMN_0_LEFT

A value to be used with the "Orientation" tag.

**See Also:**
- TAG_ORIENTATION

,

Constant Field Values

---

#### public static final int ORIENTATION_ROW_0_LEFT_COLUMN_0_TOP

A value to be used with the "Orientation" tag.

**See Also:**
- TAG_ORIENTATION

,

Constant Field Values

---

#### public static final int ORIENTATION_ROW_0_RIGHT_COLUMN_0_TOP

A value to be used with the "Orientation" tag.

**See Also:**
- TAG_ORIENTATION

,

Constant Field Values

---

#### public static final int ORIENTATION_ROW_0_RIGHT_COLUMN_0_BOTTOM

A value to be used with the "Orientation" tag.

**See Also:**
- TAG_ORIENTATION

,

Constant Field Values

---

#### public static final int ORIENTATION_ROW_0_LEFT_COLUMN_0_BOTTOM

A value to be used with the "Orientation" tag.

**See Also:**
- TAG_ORIENTATION

,

Constant Field Values

---

#### public static final int TAG_SAMPLES_PER_PIXEL

Constant specifying the "Samples_per_pixel" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_ROWS_PER_STRIP

Constant specifying the "Rows_per_strip" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_STRIP_BYTE_COUNTS

Constant specifying the "Strip_byte_counts" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_MIN_SAMPLE_VALUE

Constant specifying the "Min_sample_value" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_MAX_SAMPLE_VALUE

Constant specifying the "Max_sample_value" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_X_RESOLUTION

Constant specifying the "XResolution" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_Y_RESOLUTION

Constant specifying the "YResolution" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_PLANAR_CONFIGURATION

Constant specifying the "PlanarConfiguration" tag.

**See Also:**
- PLANAR_CONFIGURATION_CHUNKY

,

PLANAR_CONFIGURATION_PLANAR

,

Constant Field Values

---

#### public static final int PLANAR_CONFIGURATION_CHUNKY

A value to be used with the "PlanarConfiguration" tag.

**See Also:**
- TAG_PLANAR_CONFIGURATION

,

Constant Field Values

---

#### public static final int PLANAR_CONFIGURATION_PLANAR

A value to be used with the "PlanarConfiguration" tag.

**See Also:**
- TAG_PLANAR_CONFIGURATION

,

Constant Field Values

---

#### public static final int TAG_PAGE_NAME

Constant specifying the "PageName" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_X_POSITION

Constant specifying the "XPosition" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_Y_POSITION

Constant specifying the "YPosition" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_FREE_OFFSETS

Constant specifying the "FreeOffsets" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_FREE_BYTE_COUNTS

Constant specifying the "FreeByteCounts" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_GRAY_RESPONSE_UNIT

Constant specifying the "GrayResponseUnit" tag.

**See Also:**
- GRAY_RESPONSE_UNIT_TENTHS

,

GRAY_RESPONSE_UNIT_HUNDREDTHS

,

GRAY_RESPONSE_UNIT_THOUSANDTHS

,

GRAY_RESPONSE_UNIT_TEN_THOUSANDTHS

,

GRAY_RESPONSE_UNIT_HUNDRED_THOUSANDTHS

,

Constant Field Values

---

#### public static final int GRAY_RESPONSE_UNIT_TENTHS

A value to be used with the "GrayResponseUnit" tag.

**See Also:**
- TAG_GRAY_RESPONSE_UNIT

,

Constant Field Values

---

#### public static final int GRAY_RESPONSE_UNIT_HUNDREDTHS

A value to be used with the "GrayResponseUnit" tag.

**See Also:**
- TAG_GRAY_RESPONSE_UNIT

,

Constant Field Values

---

#### public static final int GRAY_RESPONSE_UNIT_THOUSANDTHS

A value to be used with the "GrayResponseUnit" tag.

**See Also:**
- TAG_GRAY_RESPONSE_UNIT

,

Constant Field Values

---

#### public static final int GRAY_RESPONSE_UNIT_TEN_THOUSANDTHS

A value to be used with the "GrayResponseUnit" tag.

**See Also:**
- TAG_GRAY_RESPONSE_UNIT

,

Constant Field Values

---

#### public static final int GRAY_RESPONSE_UNIT_HUNDRED_THOUSANDTHS

A value to be used with the "GrayResponseUnit" tag.

**See Also:**
- TAG_GRAY_RESPONSE_UNIT

,

Constant Field Values

---

#### public static final int TAG_GRAY_RESPONSE_CURVE

Constant specifying the "GrayResponseCurve" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_T4_OPTIONS

Constant specifying the "T4Options" tag.

**See Also:**
- T4_OPTIONS_2D_CODING

,

T4_OPTIONS_UNCOMPRESSED

,

T4_OPTIONS_EOL_BYTE_ALIGNED

,

Constant Field Values

---

#### public static final int T4_OPTIONS_2D_CODING

A mask to be used with the "T4Options" tag.

**See Also:**
- TAG_T4_OPTIONS

,

Constant Field Values

---

#### public static final int T4_OPTIONS_UNCOMPRESSED

A mask to be used with the "T4Options" tag.

**See Also:**
- TAG_T4_OPTIONS

,

Constant Field Values

---

#### public static final int T4_OPTIONS_EOL_BYTE_ALIGNED

A mask to be used with the "T4Options" tag.

**See Also:**
- TAG_T4_OPTIONS

,

Constant Field Values

---

#### public static final int TAG_T6_OPTIONS

Constant specifying the "T6Options" tag.

**See Also:**
- T6_OPTIONS_UNCOMPRESSED

,

Constant Field Values

---

#### public static final int T6_OPTIONS_UNCOMPRESSED

A mask to be used with the "T6Options" tag.

**See Also:**
- TAG_T6_OPTIONS

,

Constant Field Values

---

#### public static final int TAG_RESOLUTION_UNIT

Constant specifying the "ResolutionUnit" tag.

**See Also:**
- RESOLUTION_UNIT_NONE

,

RESOLUTION_UNIT_INCH

,

RESOLUTION_UNIT_CENTIMETER

,

Constant Field Values

---

#### public static final int RESOLUTION_UNIT_NONE

A value to be used with the "ResolutionUnit" tag.

**See Also:**
- TAG_RESOLUTION_UNIT

,

Constant Field Values

---

#### public static final int RESOLUTION_UNIT_INCH

A value to be used with the "ResolutionUnit" tag.

**See Also:**
- TAG_RESOLUTION_UNIT

,

Constant Field Values

---

#### public static final int RESOLUTION_UNIT_CENTIMETER

A value to be used with the "ResolutionUnit" tag.

**See Also:**
- TAG_RESOLUTION_UNIT

,

Constant Field Values

---

#### public static final int TAG_PAGE_NUMBER

Constant specifying the "PageNumber" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_TRANSFER_FUNCTION

Constant specifying the "TransferFunction" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_SOFTWARE

Constant specifying the "Software" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_DATE_TIME

Constant specifying the "DateTime" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_ARTIST

Constant specifying the "Artist" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_HOST_COMPUTER

Constant specifying the "HostComputer" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_PREDICTOR

Constant specifying the "Predictor" tag.

**See Also:**
- TAG_WHITE_POINT

,

TAG_PRIMARY_CHROMATICITES

,

TAG_COLOR_MAP

,

TAG_HALFTONE_HINTS

,

TAG_TILE_WIDTH

,

TAG_TILE_LENGTH

,

TAG_TILE_OFFSETS

,

TAG_TILE_BYTE_COUNTS

,

Constant Field Values

---

#### public static final int PREDICTOR_NONE

A value to be used with the "Predictor" tag.

**See Also:**
- TAG_PREDICTOR

,

Constant Field Values

---

#### public static final int PREDICTOR_HORIZONTAL_DIFFERENCING

A value to be used with the "Predictor" tag.

**See Also:**
- TAG_PREDICTOR

,

Constant Field Values

---

#### public static final int TAG_WHITE_POINT

Constant specifying the "WhitePoint" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_PRIMARY_CHROMATICITES

Constant specifying the "PrimaryChromaticites" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_COLOR_MAP

Constant specifying the "ColorMap" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_HALFTONE_HINTS

Constant specifying the "HalftoneHints" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_TILE_WIDTH

Constant specifying the "TileWidth" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_TILE_LENGTH

Constant specifying the "TileLength" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_TILE_OFFSETS

Constant specifying the "TileOffsets" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_TILE_BYTE_COUNTS

Constant specifying the "TileByteCounts" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_INK_SET

Constant specifying the "InkSet" tag.

**See Also:**
- INK_SET_CMYK

,

INK_SET_NOT_CMYK

,

Constant Field Values

---

#### public static final int INK_SET_CMYK

A value to be used with the "InkSet" tag.

**See Also:**
- TAG_INK_SET

,

Constant Field Values

---

#### public static final int INK_SET_NOT_CMYK

A value to be used with the "InkSet" tag.

**See Also:**
- TAG_INK_SET

,

Constant Field Values

---

#### public static final int TAG_INK_NAMES

Constant specifying the "InkNames" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_NUMBER_OF_INKS

Constant specifying the "NumberOfInks" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_DOT_RANGE

Constant specifying the "DotRange" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_TARGET_PRINTER

Constant specifying the "TargetPrinter" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_EXTRA_SAMPLES

Constant specifying the "ExtraSamples" tag.

**See Also:**
- EXTRA_SAMPLES_UNSPECIFIED

,

EXTRA_SAMPLES_ASSOCIATED_ALPHA

,

EXTRA_SAMPLES_UNASSOCIATED_ALPHA

,

Constant Field Values

---

#### public static final int EXTRA_SAMPLES_UNSPECIFIED

A value to be used with the "ExtraSamples" tag.

**See Also:**
- TAG_EXTRA_SAMPLES

,

Constant Field Values

---

#### public static final int EXTRA_SAMPLES_ASSOCIATED_ALPHA

A value to be used with the "ExtraSamples" tag.

**See Also:**
- TAG_EXTRA_SAMPLES

,

Constant Field Values

---

#### public static final int EXTRA_SAMPLES_UNASSOCIATED_ALPHA

A value to be used with the "ExtraSamples" tag.

**See Also:**
- TAG_EXTRA_SAMPLES

,

Constant Field Values

---

#### public static final int TAG_SAMPLE_FORMAT

Constant specifying the "SampleFormat" tag.

**See Also:**
- SAMPLE_FORMAT_UNSIGNED_INTEGER

,

SAMPLE_FORMAT_SIGNED_INTEGER

,

SAMPLE_FORMAT_FLOATING_POINT

,

SAMPLE_FORMAT_UNDEFINED

,

Constant Field Values

---

#### public static final int SAMPLE_FORMAT_UNSIGNED_INTEGER

A value to be used with the "SampleFormat" tag.

**See Also:**
- TAG_SAMPLE_FORMAT

,

Constant Field Values

---

#### public static final int SAMPLE_FORMAT_SIGNED_INTEGER

A value to be used with the "SampleFormat" tag.

**See Also:**
- TAG_SAMPLE_FORMAT

,

Constant Field Values

---

#### public static final int SAMPLE_FORMAT_FLOATING_POINT

A value to be used with the "SampleFormat" tag.

**See Also:**
- TAG_SAMPLE_FORMAT

,

Constant Field Values

---

#### public static final int SAMPLE_FORMAT_UNDEFINED

A value to be used with the "SampleFormat" tag.

**See Also:**
- TAG_SAMPLE_FORMAT

,

Constant Field Values

---

#### public static final int TAG_S_MIN_SAMPLE_VALUE

Constant specifying the "SMinSampleValue" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_S_MAX_SAMPLE_VALUE

Constant specifying the "SMaxSampleValue" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_TRANSFER_RANGE

Constant specifying the "TransferRange" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_JPEG_TABLES

Constant specifying the "JPEGTables" tag.

**See Also:**
- JPEG-in-TIFF compression

,

Constant Field Values

---

#### public static final int TAG_JPEG_PROC

Constant specifying the "JPEGProc" tag.

**See Also:**
- Constant Field Values

---

#### public static final int JPEG_PROC_BASELINE

A value to be used with the "JPEGProc" tag.

**See Also:**
- TAG_JPEG_PROC

,

Constant Field Values

---

#### public static final int JPEG_PROC_LOSSLESS

A value to be used with the "JPEGProc" tag.

**See Also:**
- TAG_JPEG_PROC

,

Constant Field Values

---

#### public static final int TAG_JPEG_INTERCHANGE_FORMAT

Constant specifying the "JPEGInterchangeFormat" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_JPEG_INTERCHANGE_FORMAT_LENGTH

Constant specifying the "JPEGInterchangeFormatLength" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_JPEG_RESTART_INTERVAL

Constant specifying the "JPEGRestartInterval" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_JPEG_LOSSLESS_PREDICTORS

Constant specifying the "JPEGLosslessPredictors" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_JPEG_POINT_TRANSFORMS

Constant specifying the "JPEGPointTransforms" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_JPEG_Q_TABLES

Constant specifying the "JPEGQTables" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_JPEG_DC_TABLES

Constant specifying the "JPEGDCTables" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_JPEG_AC_TABLES

Constant specifying the "JPEGACTables" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_Y_CB_CR_COEFFICIENTS

Constant specifying the "YCbCrCoefficients" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_Y_CB_CR_SUBSAMPLING

Constant specifying the "YCbCrSubsampling" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_Y_CB_CR_POSITIONING

Constant specifying the "YCbCrPositioning" tag.

**See Also:**
- Y_CB_CR_POSITIONING_CENTERED

,

Y_CB_CR_POSITIONING_COSITED

,

Constant Field Values

---

#### public static final int Y_CB_CR_POSITIONING_CENTERED

A value to be used with the "YCbCrPositioning" tag.

**See Also:**
- TAG_Y_CB_CR_POSITIONING

,

Constant Field Values

---

#### public static final int Y_CB_CR_POSITIONING_COSITED

A value to be used with the "YCbCrPositioning" tag.

**See Also:**
- TAG_Y_CB_CR_POSITIONING

,

Constant Field Values

---

#### public static final int TAG_REFERENCE_BLACK_WHITE

Constant specifying the "ReferenceBlackWhite" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_COPYRIGHT

Constant specifying the "Copyright" tag.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_ICC_PROFILE

Constant specifying the "ICC Profile" tag.

**See Also:**
- ICC Specification, section B.4: Embedding ICC profiles in TIFF files

,

Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### public static
BaselineTIFFTagSet
getInstance()

Returns a shared instance of a

BaselineTIFFTagSet

.

**Returns:**
- a

BaselineTIFFTagSet

instance.

---

### Additional Sections

#### Class BaselineTIFFTagSet

java.lang.Object

- javax.imageio.plugins.tiff.TIFFTagSet
- - javax.imageio.plugins.tiff.BaselineTIFFTagSet

javax.imageio.plugins.tiff.TIFFTagSet

- javax.imageio.plugins.tiff.BaselineTIFFTagSet

javax.imageio.plugins.tiff.BaselineTIFFTagSet

```java
public final class
BaselineTIFFTagSet

extends
TIFFTagSet
```

A class representing the set of tags found in the baseline TIFF
specification as well as some common additional tags.

The non-baseline tags included in this class are:

- JPEGTables

ICC Profile

The non-baseline values of baseline tags included in this class are

- Compression

tag values:

- JPEG-in-TIFF compression
- Zlib-in-TIFF compression
- Deflate compression
- PhotometricInterpretation

tag values:

- ICCLAB
photometric interpretation

**Since:** 9
**See Also:** TIFF 6.0 Specification

public final class

BaselineTIFFTagSet

extends

TIFFTagSet

A class representing the set of tags found in the baseline TIFF
specification as well as some common additional tags.

The non-baseline tags included in this class are:

- JPEGTables

ICC Profile

The non-baseline values of baseline tags included in this class are

- Compression

tag values:

- JPEG-in-TIFF compression
- Zlib-in-TIFF compression
- Deflate compression
- PhotometricInterpretation

tag values:

- ICCLAB
photometric interpretation

The non-baseline tags included in this class are:

- JPEGTables

ICC Profile

The non-baseline values of baseline tags included in this class are

- Compression

tag values:

- JPEG-in-TIFF compression
- Zlib-in-TIFF compression
- Deflate compression
- PhotometricInterpretation

tag values:

- ICCLAB
photometric interpretation

JPEGTables

ICC Profile

The non-baseline values of baseline tags included in this class are

- Compression

tag values:

- JPEG-in-TIFF compression
- Zlib-in-TIFF compression
- Deflate compression
- PhotometricInterpretation

tag values:

- ICCLAB
photometric interpretation

Compression

tag values:

- JPEG-in-TIFF compression
- Zlib-in-TIFF compression
- Deflate compression

PhotometricInterpretation

tag values:

- ICCLAB
photometric interpretation

JPEG-in-TIFF compression

Zlib-in-TIFF compression

Deflate compression

ICCLAB
photometric interpretation

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

COMPRESSION_CCITT_RLE

A value to be used with the "Compression" tag.

static int

COMPRESSION_CCITT_T_4

A value to be used with the "Compression" tag.

static int

COMPRESSION_CCITT_T_6

A value to be used with the "Compression" tag.

static int

COMPRESSION_DEFLATE

A value to be used with the "Compression" tag.

static int

COMPRESSION_JPEG

A value to be used with the "Compression" tag.

static int

COMPRESSION_LZW

A value to be used with the "Compression" tag.

static int

COMPRESSION_NONE

A value to be used with the "Compression" tag.

static int

COMPRESSION_OLD_JPEG

A value to be used with the "Compression" tag.

static int

COMPRESSION_PACKBITS

A value to be used with the "Compression" tag.

static int

COMPRESSION_ZLIB

A value to be used with the "Compression" tag.

static int

EXTRA_SAMPLES_ASSOCIATED_ALPHA

A value to be used with the "ExtraSamples" tag.

static int

EXTRA_SAMPLES_UNASSOCIATED_ALPHA

A value to be used with the "ExtraSamples" tag.

static int

EXTRA_SAMPLES_UNSPECIFIED

A value to be used with the "ExtraSamples" tag.

static int

FILL_ORDER_LEFT_TO_RIGHT

A value to be used with the "FillOrder" tag.

static int

FILL_ORDER_RIGHT_TO_LEFT

A value to be used with the "FillOrder" tag.

static int

GRAY_RESPONSE_UNIT_HUNDRED_THOUSANDTHS

A value to be used with the "GrayResponseUnit" tag.

static int

GRAY_RESPONSE_UNIT_HUNDREDTHS

A value to be used with the "GrayResponseUnit" tag.

static int

GRAY_RESPONSE_UNIT_TEN_THOUSANDTHS

A value to be used with the "GrayResponseUnit" tag.

static int

GRAY_RESPONSE_UNIT_TENTHS

A value to be used with the "GrayResponseUnit" tag.

static int

GRAY_RESPONSE_UNIT_THOUSANDTHS

A value to be used with the "GrayResponseUnit" tag.

static int

INK_SET_CMYK

A value to be used with the "InkSet" tag.

static int

INK_SET_NOT_CMYK

A value to be used with the "InkSet" tag.

static int

JPEG_PROC_BASELINE

A value to be used with the "JPEGProc" tag.

static int

JPEG_PROC_LOSSLESS

A value to be used with the "JPEGProc" tag.

static int

NEW_SUBFILE_TYPE_REDUCED_RESOLUTION

A mask to be used with the "NewSubfileType" tag.

static int

NEW_SUBFILE_TYPE_SINGLE_PAGE

A mask to be used with the "NewSubfileType" tag.

static int

NEW_SUBFILE_TYPE_TRANSPARENCY

A mask to be used with the "NewSubfileType" tag.

static int

ORIENTATION_ROW_0_BOTTOM_COLUMN_0_LEFT

A value to be used with the "Orientation" tag.

static int

ORIENTATION_ROW_0_BOTTOM_COLUMN_0_RIGHT

A value to be used with the "Orientation" tag.

static int

ORIENTATION_ROW_0_LEFT_COLUMN_0_BOTTOM

A value to be used with the "Orientation" tag.

static int

ORIENTATION_ROW_0_LEFT_COLUMN_0_TOP

A value to be used with the "Orientation" tag.

static int

ORIENTATION_ROW_0_RIGHT_COLUMN_0_BOTTOM

A value to be used with the "Orientation" tag.

static int

ORIENTATION_ROW_0_RIGHT_COLUMN_0_TOP

A value to be used with the "Orientation" tag.

static int

ORIENTATION_ROW_0_TOP_COLUMN_0_LEFT

A value to be used with the "Orientation" tag.

static int

ORIENTATION_ROW_0_TOP_COLUMN_0_RIGHT

A value to be used with the "Orientation" tag.

static int

PHOTOMETRIC_INTERPRETATION_BLACK_IS_ZERO

A value to be used with the "PhotometricInterpretation" tag.

static int

PHOTOMETRIC_INTERPRETATION_CIELAB

A value to be used with the "PhotometricInterpretation" tag.

static int

PHOTOMETRIC_INTERPRETATION_CMYK

A value to be used with the "PhotometricInterpretation" tag.

static int

PHOTOMETRIC_INTERPRETATION_ICCLAB

A value to be used with the "PhotometricInterpretation" tag.

static int

PHOTOMETRIC_INTERPRETATION_PALETTE_COLOR

A value to be used with the "PhotometricInterpretation" tag.

static int

PHOTOMETRIC_INTERPRETATION_RGB

A value to be used with the "PhotometricInterpretation" tag.

static int

PHOTOMETRIC_INTERPRETATION_TRANSPARENCY_MASK

A value to be used with the "PhotometricInterpretation" tag.

static int

PHOTOMETRIC_INTERPRETATION_WHITE_IS_ZERO

A value to be used with the "PhotometricInterpretation" tag.

static int

PHOTOMETRIC_INTERPRETATION_Y_CB_CR

A value to be used with the "PhotometricInterpretation" tag.

static int

PLANAR_CONFIGURATION_CHUNKY

A value to be used with the "PlanarConfiguration" tag.

static int

PLANAR_CONFIGURATION_PLANAR

A value to be used with the "PlanarConfiguration" tag.

static int

PREDICTOR_HORIZONTAL_DIFFERENCING

A value to be used with the "Predictor" tag.

static int

PREDICTOR_NONE

A value to be used with the "Predictor" tag.

static int

RESOLUTION_UNIT_CENTIMETER

A value to be used with the "ResolutionUnit" tag.

static int

RESOLUTION_UNIT_INCH

A value to be used with the "ResolutionUnit" tag.

static int

RESOLUTION_UNIT_NONE

A value to be used with the "ResolutionUnit" tag.

static int

SAMPLE_FORMAT_FLOATING_POINT

A value to be used with the "SampleFormat" tag.

static int

SAMPLE_FORMAT_SIGNED_INTEGER

A value to be used with the "SampleFormat" tag.

static int

SAMPLE_FORMAT_UNDEFINED

A value to be used with the "SampleFormat" tag.

static int

SAMPLE_FORMAT_UNSIGNED_INTEGER

A value to be used with the "SampleFormat" tag.

static int

SUBFILE_TYPE_FULL_RESOLUTION

A value to be used with the "SubfileType" tag.

static int

SUBFILE_TYPE_REDUCED_RESOLUTION

A value to be used with the "SubfileType" tag.

static int

SUBFILE_TYPE_SINGLE_PAGE

A value to be used with the "SubfileType" tag.

static int

T4_OPTIONS_2D_CODING

A mask to be used with the "T4Options" tag.

static int

T4_OPTIONS_EOL_BYTE_ALIGNED

A mask to be used with the "T4Options" tag.

static int

T4_OPTIONS_UNCOMPRESSED

A mask to be used with the "T4Options" tag.

static int

T6_OPTIONS_UNCOMPRESSED

A mask to be used with the "T6Options" tag.

static int

TAG_ARTIST

Constant specifying the "Artist" tag.

static int

TAG_BITS_PER_SAMPLE

Constant specifying the "BitsPerSample" tag.

static int

TAG_CELL_LENGTH

Constant specifying the "cell_length" tag.

static int

TAG_CELL_WIDTH

Constant specifying the "Cell_Width" tag.

static int

TAG_COLOR_MAP

Constant specifying the "ColorMap" tag.

static int

TAG_COMPRESSION

Constant specifying the "Compression" tag.

static int

TAG_COPYRIGHT

Constant specifying the "Copyright" tag.

static int

TAG_DATE_TIME

Constant specifying the "DateTime" tag.

static int

TAG_DOCUMENT_NAME

Constant specifying the "document_name" tag.

static int

TAG_DOT_RANGE

Constant specifying the "DotRange" tag.

static int

TAG_EXTRA_SAMPLES

Constant specifying the "ExtraSamples" tag.

static int

TAG_FILL_ORDER

Constant specifying the "fill_order" tag.

static int

TAG_FREE_BYTE_COUNTS

Constant specifying the "FreeByteCounts" tag.

static int

TAG_FREE_OFFSETS

Constant specifying the "FreeOffsets" tag.

static int

TAG_GRAY_RESPONSE_CURVE

Constant specifying the "GrayResponseCurve" tag.

static int

TAG_GRAY_RESPONSE_UNIT

Constant specifying the "GrayResponseUnit" tag.

static int

TAG_HALFTONE_HINTS

Constant specifying the "HalftoneHints" tag.

static int

TAG_HOST_COMPUTER

Constant specifying the "HostComputer" tag.

static int

TAG_ICC_PROFILE

Constant specifying the "ICC Profile" tag.

static int

TAG_IMAGE_DESCRIPTION

Constant specifying the "Image_description" tag.

static int

TAG_IMAGE_LENGTH

Constant specifying the "ImageLength" tag.

static int

TAG_IMAGE_WIDTH

Constant specifying the "ImageWidth" tag.

static int

TAG_INK_NAMES

Constant specifying the "InkNames" tag.

static int

TAG_INK_SET

Constant specifying the "InkSet" tag.

static int

TAG_JPEG_AC_TABLES

Constant specifying the "JPEGACTables" tag.

static int

TAG_JPEG_DC_TABLES

Constant specifying the "JPEGDCTables" tag.

static int

TAG_JPEG_INTERCHANGE_FORMAT

Constant specifying the "JPEGInterchangeFormat" tag.

static int

TAG_JPEG_INTERCHANGE_FORMAT_LENGTH

Constant specifying the "JPEGInterchangeFormatLength" tag.

static int

TAG_JPEG_LOSSLESS_PREDICTORS

Constant specifying the "JPEGLosslessPredictors" tag.

static int

TAG_JPEG_POINT_TRANSFORMS

Constant specifying the "JPEGPointTransforms" tag.

static int

TAG_JPEG_PROC

Constant specifying the "JPEGProc" tag.

static int

TAG_JPEG_Q_TABLES

Constant specifying the "JPEGQTables" tag.

static int

TAG_JPEG_RESTART_INTERVAL

Constant specifying the "JPEGRestartInterval" tag.

static int

TAG_JPEG_TABLES

Constant specifying the "JPEGTables" tag.

static int

TAG_MAKE

Constant specifying the "Make" tag.

static int

TAG_MAX_SAMPLE_VALUE

Constant specifying the "Max_sample_value" tag.

static int

TAG_MIN_SAMPLE_VALUE

Constant specifying the "Min_sample_value" tag.

static int

TAG_MODEL

Constant specifying the "Model" tag.

static int

TAG_NEW_SUBFILE_TYPE

Constant specifying the "NewSubfileType" tag.

static int

TAG_NUMBER_OF_INKS

Constant specifying the "NumberOfInks" tag.

static int

TAG_ORIENTATION

Constant specifying the "Orientation" tag.

static int

TAG_PAGE_NAME

Constant specifying the "PageName" tag.

static int

TAG_PAGE_NUMBER

Constant specifying the "PageNumber" tag.

static int

TAG_PHOTOMETRIC_INTERPRETATION

Constant specifying the "PhotometricInterpretation" tag.

static int

TAG_PLANAR_CONFIGURATION

Constant specifying the "PlanarConfiguration" tag.

static int

TAG_PREDICTOR

Constant specifying the "Predictor" tag.

static int

TAG_PRIMARY_CHROMATICITES

Constant specifying the "PrimaryChromaticites" tag.

static int

TAG_REFERENCE_BLACK_WHITE

Constant specifying the "ReferenceBlackWhite" tag.

static int

TAG_RESOLUTION_UNIT

Constant specifying the "ResolutionUnit" tag.

static int

TAG_ROWS_PER_STRIP

Constant specifying the "Rows_per_strip" tag.

static int

TAG_S_MAX_SAMPLE_VALUE

Constant specifying the "SMaxSampleValue" tag.

static int

TAG_S_MIN_SAMPLE_VALUE

Constant specifying the "SMinSampleValue" tag.

static int

TAG_SAMPLE_FORMAT

Constant specifying the "SampleFormat" tag.

static int

TAG_SAMPLES_PER_PIXEL

Constant specifying the "Samples_per_pixel" tag.

static int

TAG_SOFTWARE

Constant specifying the "Software" tag.

static int

TAG_STRIP_BYTE_COUNTS

Constant specifying the "Strip_byte_counts" tag.

static int

TAG_STRIP_OFFSETS

Constant specifying the "Strip_offsets" tag.

static int

TAG_SUBFILE_TYPE

Constant specifying the "SubfileType" tag.

static int

TAG_T4_OPTIONS

Constant specifying the "T4Options" tag.

static int

TAG_T6_OPTIONS

Constant specifying the "T6Options" tag.

static int

TAG_TARGET_PRINTER

Constant specifying the "TargetPrinter" tag.

static int

TAG_THRESHHOLDING

Constant specifying the "Threshholding" tag.

static int

TAG_TILE_BYTE_COUNTS

Constant specifying the "TileByteCounts" tag.

static int

TAG_TILE_LENGTH

Constant specifying the "TileLength" tag.

static int

TAG_TILE_OFFSETS

Constant specifying the "TileOffsets" tag.

static int

TAG_TILE_WIDTH

Constant specifying the "TileWidth" tag.

static int

TAG_TRANSFER_FUNCTION

Constant specifying the "TransferFunction" tag.

static int

TAG_TRANSFER_RANGE

Constant specifying the "TransferRange" tag.

static int

TAG_WHITE_POINT

Constant specifying the "WhitePoint" tag.

static int

TAG_X_POSITION

Constant specifying the "XPosition" tag.

static int

TAG_X_RESOLUTION

Constant specifying the "XResolution" tag.

static int

TAG_Y_CB_CR_COEFFICIENTS

Constant specifying the "YCbCrCoefficients" tag.

static int

TAG_Y_CB_CR_POSITIONING

Constant specifying the "YCbCrPositioning" tag.

static int

TAG_Y_CB_CR_SUBSAMPLING

Constant specifying the "YCbCrSubsampling" tag.

static int

TAG_Y_POSITION

Constant specifying the "YPosition" tag.

static int

TAG_Y_RESOLUTION

Constant specifying the "YResolution" tag.

static int

THRESHHOLDING_NONE

A value to be used with the "Thresholding" tag.

static int

THRESHHOLDING_ORDERED_DITHER

A value to be used with the "Thresholding" tag.

static int

THRESHHOLDING_RANDOMIZED_DITHER

A value to be used with the "Thresholding" tag.

static int

Y_CB_CR_POSITIONING_CENTERED

A value to be used with the "YCbCrPositioning" tag.

static int

Y_CB_CR_POSITIONING_COSITED

A value to be used with the "YCbCrPositioning" tag.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

BaselineTIFFTagSet

getInstance

()

Returns a shared instance of a

BaselineTIFFTagSet

.

- Methods declared in class javax.imageio.plugins.tiff.

TIFFTagSet

getTag

,

getTag

,

getTagNames

,

getTagNumbers

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

Field Summary

Fields

Modifier and Type

Field

Description

static int

COMPRESSION_CCITT_RLE

A value to be used with the "Compression" tag.

static int

COMPRESSION_CCITT_T_4

A value to be used with the "Compression" tag.

static int

COMPRESSION_CCITT_T_6

A value to be used with the "Compression" tag.

static int

COMPRESSION_DEFLATE

A value to be used with the "Compression" tag.

static int

COMPRESSION_JPEG

A value to be used with the "Compression" tag.

static int

COMPRESSION_LZW

A value to be used with the "Compression" tag.

static int

COMPRESSION_NONE

A value to be used with the "Compression" tag.

static int

COMPRESSION_OLD_JPEG

A value to be used with the "Compression" tag.

static int

COMPRESSION_PACKBITS

A value to be used with the "Compression" tag.

static int

COMPRESSION_ZLIB

A value to be used with the "Compression" tag.

static int

EXTRA_SAMPLES_ASSOCIATED_ALPHA

A value to be used with the "ExtraSamples" tag.

static int

EXTRA_SAMPLES_UNASSOCIATED_ALPHA

A value to be used with the "ExtraSamples" tag.

static int

EXTRA_SAMPLES_UNSPECIFIED

A value to be used with the "ExtraSamples" tag.

static int

FILL_ORDER_LEFT_TO_RIGHT

A value to be used with the "FillOrder" tag.

static int

FILL_ORDER_RIGHT_TO_LEFT

A value to be used with the "FillOrder" tag.

static int

GRAY_RESPONSE_UNIT_HUNDRED_THOUSANDTHS

A value to be used with the "GrayResponseUnit" tag.

static int

GRAY_RESPONSE_UNIT_HUNDREDTHS

A value to be used with the "GrayResponseUnit" tag.

static int

GRAY_RESPONSE_UNIT_TEN_THOUSANDTHS

A value to be used with the "GrayResponseUnit" tag.

static int

GRAY_RESPONSE_UNIT_TENTHS

A value to be used with the "GrayResponseUnit" tag.

static int

GRAY_RESPONSE_UNIT_THOUSANDTHS

A value to be used with the "GrayResponseUnit" tag.

static int

INK_SET_CMYK

A value to be used with the "InkSet" tag.

static int

INK_SET_NOT_CMYK

A value to be used with the "InkSet" tag.

static int

JPEG_PROC_BASELINE

A value to be used with the "JPEGProc" tag.

static int

JPEG_PROC_LOSSLESS

A value to be used with the "JPEGProc" tag.

static int

NEW_SUBFILE_TYPE_REDUCED_RESOLUTION

A mask to be used with the "NewSubfileType" tag.

static int

NEW_SUBFILE_TYPE_SINGLE_PAGE

A mask to be used with the "NewSubfileType" tag.

static int

NEW_SUBFILE_TYPE_TRANSPARENCY

A mask to be used with the "NewSubfileType" tag.

static int

ORIENTATION_ROW_0_BOTTOM_COLUMN_0_LEFT

A value to be used with the "Orientation" tag.

static int

ORIENTATION_ROW_0_BOTTOM_COLUMN_0_RIGHT

A value to be used with the "Orientation" tag.

static int

ORIENTATION_ROW_0_LEFT_COLUMN_0_BOTTOM

A value to be used with the "Orientation" tag.

static int

ORIENTATION_ROW_0_LEFT_COLUMN_0_TOP

A value to be used with the "Orientation" tag.

static int

ORIENTATION_ROW_0_RIGHT_COLUMN_0_BOTTOM

A value to be used with the "Orientation" tag.

static int

ORIENTATION_ROW_0_RIGHT_COLUMN_0_TOP

A value to be used with the "Orientation" tag.

static int

ORIENTATION_ROW_0_TOP_COLUMN_0_LEFT

A value to be used with the "Orientation" tag.

static int

ORIENTATION_ROW_0_TOP_COLUMN_0_RIGHT

A value to be used with the "Orientation" tag.

static int

PHOTOMETRIC_INTERPRETATION_BLACK_IS_ZERO

A value to be used with the "PhotometricInterpretation" tag.

static int

PHOTOMETRIC_INTERPRETATION_CIELAB

A value to be used with the "PhotometricInterpretation" tag.

static int

PHOTOMETRIC_INTERPRETATION_CMYK

A value to be used with the "PhotometricInterpretation" tag.

static int

PHOTOMETRIC_INTERPRETATION_ICCLAB

A value to be used with the "PhotometricInterpretation" tag.

static int

PHOTOMETRIC_INTERPRETATION_PALETTE_COLOR

A value to be used with the "PhotometricInterpretation" tag.

static int

PHOTOMETRIC_INTERPRETATION_RGB

A value to be used with the "PhotometricInterpretation" tag.

static int

PHOTOMETRIC_INTERPRETATION_TRANSPARENCY_MASK

A value to be used with the "PhotometricInterpretation" tag.

static int

PHOTOMETRIC_INTERPRETATION_WHITE_IS_ZERO

A value to be used with the "PhotometricInterpretation" tag.

static int

PHOTOMETRIC_INTERPRETATION_Y_CB_CR

A value to be used with the "PhotometricInterpretation" tag.

static int

PLANAR_CONFIGURATION_CHUNKY

A value to be used with the "PlanarConfiguration" tag.

static int

PLANAR_CONFIGURATION_PLANAR

A value to be used with the "PlanarConfiguration" tag.

static int

PREDICTOR_HORIZONTAL_DIFFERENCING

A value to be used with the "Predictor" tag.

static int

PREDICTOR_NONE

A value to be used with the "Predictor" tag.

static int

RESOLUTION_UNIT_CENTIMETER

A value to be used with the "ResolutionUnit" tag.

static int

RESOLUTION_UNIT_INCH

A value to be used with the "ResolutionUnit" tag.

static int

RESOLUTION_UNIT_NONE

A value to be used with the "ResolutionUnit" tag.

static int

SAMPLE_FORMAT_FLOATING_POINT

A value to be used with the "SampleFormat" tag.

static int

SAMPLE_FORMAT_SIGNED_INTEGER

A value to be used with the "SampleFormat" tag.

static int

SAMPLE_FORMAT_UNDEFINED

A value to be used with the "SampleFormat" tag.

static int

SAMPLE_FORMAT_UNSIGNED_INTEGER

A value to be used with the "SampleFormat" tag.

static int

SUBFILE_TYPE_FULL_RESOLUTION

A value to be used with the "SubfileType" tag.

static int

SUBFILE_TYPE_REDUCED_RESOLUTION

A value to be used with the "SubfileType" tag.

static int

SUBFILE_TYPE_SINGLE_PAGE

A value to be used with the "SubfileType" tag.

static int

T4_OPTIONS_2D_CODING

A mask to be used with the "T4Options" tag.

static int

T4_OPTIONS_EOL_BYTE_ALIGNED

A mask to be used with the "T4Options" tag.

static int

T4_OPTIONS_UNCOMPRESSED

A mask to be used with the "T4Options" tag.

static int

T6_OPTIONS_UNCOMPRESSED

A mask to be used with the "T6Options" tag.

static int

TAG_ARTIST

Constant specifying the "Artist" tag.

static int

TAG_BITS_PER_SAMPLE

Constant specifying the "BitsPerSample" tag.

static int

TAG_CELL_LENGTH

Constant specifying the "cell_length" tag.

static int

TAG_CELL_WIDTH

Constant specifying the "Cell_Width" tag.

static int

TAG_COLOR_MAP

Constant specifying the "ColorMap" tag.

static int

TAG_COMPRESSION

Constant specifying the "Compression" tag.

static int

TAG_COPYRIGHT

Constant specifying the "Copyright" tag.

static int

TAG_DATE_TIME

Constant specifying the "DateTime" tag.

static int

TAG_DOCUMENT_NAME

Constant specifying the "document_name" tag.

static int

TAG_DOT_RANGE

Constant specifying the "DotRange" tag.

static int

TAG_EXTRA_SAMPLES

Constant specifying the "ExtraSamples" tag.

static int

TAG_FILL_ORDER

Constant specifying the "fill_order" tag.

static int

TAG_FREE_BYTE_COUNTS

Constant specifying the "FreeByteCounts" tag.

static int

TAG_FREE_OFFSETS

Constant specifying the "FreeOffsets" tag.

static int

TAG_GRAY_RESPONSE_CURVE

Constant specifying the "GrayResponseCurve" tag.

static int

TAG_GRAY_RESPONSE_UNIT

Constant specifying the "GrayResponseUnit" tag.

static int

TAG_HALFTONE_HINTS

Constant specifying the "HalftoneHints" tag.

static int

TAG_HOST_COMPUTER

Constant specifying the "HostComputer" tag.

static int

TAG_ICC_PROFILE

Constant specifying the "ICC Profile" tag.

static int

TAG_IMAGE_DESCRIPTION

Constant specifying the "Image_description" tag.

static int

TAG_IMAGE_LENGTH

Constant specifying the "ImageLength" tag.

static int

TAG_IMAGE_WIDTH

Constant specifying the "ImageWidth" tag.

static int

TAG_INK_NAMES

Constant specifying the "InkNames" tag.

static int

TAG_INK_SET

Constant specifying the "InkSet" tag.

static int

TAG_JPEG_AC_TABLES

Constant specifying the "JPEGACTables" tag.

static int

TAG_JPEG_DC_TABLES

Constant specifying the "JPEGDCTables" tag.

static int

TAG_JPEG_INTERCHANGE_FORMAT

Constant specifying the "JPEGInterchangeFormat" tag.

static int

TAG_JPEG_INTERCHANGE_FORMAT_LENGTH

Constant specifying the "JPEGInterchangeFormatLength" tag.

static int

TAG_JPEG_LOSSLESS_PREDICTORS

Constant specifying the "JPEGLosslessPredictors" tag.

static int

TAG_JPEG_POINT_TRANSFORMS

Constant specifying the "JPEGPointTransforms" tag.

static int

TAG_JPEG_PROC

Constant specifying the "JPEGProc" tag.

static int

TAG_JPEG_Q_TABLES

Constant specifying the "JPEGQTables" tag.

static int

TAG_JPEG_RESTART_INTERVAL

Constant specifying the "JPEGRestartInterval" tag.

static int

TAG_JPEG_TABLES

Constant specifying the "JPEGTables" tag.

static int

TAG_MAKE

Constant specifying the "Make" tag.

static int

TAG_MAX_SAMPLE_VALUE

Constant specifying the "Max_sample_value" tag.

static int

TAG_MIN_SAMPLE_VALUE

Constant specifying the "Min_sample_value" tag.

static int

TAG_MODEL

Constant specifying the "Model" tag.

static int

TAG_NEW_SUBFILE_TYPE

Constant specifying the "NewSubfileType" tag.

static int

TAG_NUMBER_OF_INKS

Constant specifying the "NumberOfInks" tag.

static int

TAG_ORIENTATION

Constant specifying the "Orientation" tag.

static int

TAG_PAGE_NAME

Constant specifying the "PageName" tag.

static int

TAG_PAGE_NUMBER

Constant specifying the "PageNumber" tag.

static int

TAG_PHOTOMETRIC_INTERPRETATION

Constant specifying the "PhotometricInterpretation" tag.

static int

TAG_PLANAR_CONFIGURATION

Constant specifying the "PlanarConfiguration" tag.

static int

TAG_PREDICTOR

Constant specifying the "Predictor" tag.

static int

TAG_PRIMARY_CHROMATICITES

Constant specifying the "PrimaryChromaticites" tag.

static int

TAG_REFERENCE_BLACK_WHITE

Constant specifying the "ReferenceBlackWhite" tag.

static int

TAG_RESOLUTION_UNIT

Constant specifying the "ResolutionUnit" tag.

static int

TAG_ROWS_PER_STRIP

Constant specifying the "Rows_per_strip" tag.

static int

TAG_S_MAX_SAMPLE_VALUE

Constant specifying the "SMaxSampleValue" tag.

static int

TAG_S_MIN_SAMPLE_VALUE

Constant specifying the "SMinSampleValue" tag.

static int

TAG_SAMPLE_FORMAT

Constant specifying the "SampleFormat" tag.

static int

TAG_SAMPLES_PER_PIXEL

Constant specifying the "Samples_per_pixel" tag.

static int

TAG_SOFTWARE

Constant specifying the "Software" tag.

static int

TAG_STRIP_BYTE_COUNTS

Constant specifying the "Strip_byte_counts" tag.

static int

TAG_STRIP_OFFSETS

Constant specifying the "Strip_offsets" tag.

static int

TAG_SUBFILE_TYPE

Constant specifying the "SubfileType" tag.

static int

TAG_T4_OPTIONS

Constant specifying the "T4Options" tag.

static int

TAG_T6_OPTIONS

Constant specifying the "T6Options" tag.

static int

TAG_TARGET_PRINTER

Constant specifying the "TargetPrinter" tag.

static int

TAG_THRESHHOLDING

Constant specifying the "Threshholding" tag.

static int

TAG_TILE_BYTE_COUNTS

Constant specifying the "TileByteCounts" tag.

static int

TAG_TILE_LENGTH

Constant specifying the "TileLength" tag.

static int

TAG_TILE_OFFSETS

Constant specifying the "TileOffsets" tag.

static int

TAG_TILE_WIDTH

Constant specifying the "TileWidth" tag.

static int

TAG_TRANSFER_FUNCTION

Constant specifying the "TransferFunction" tag.

static int

TAG_TRANSFER_RANGE

Constant specifying the "TransferRange" tag.

static int

TAG_WHITE_POINT

Constant specifying the "WhitePoint" tag.

static int

TAG_X_POSITION

Constant specifying the "XPosition" tag.

static int

TAG_X_RESOLUTION

Constant specifying the "XResolution" tag.

static int

TAG_Y_CB_CR_COEFFICIENTS

Constant specifying the "YCbCrCoefficients" tag.

static int

TAG_Y_CB_CR_POSITIONING

Constant specifying the "YCbCrPositioning" tag.

static int

TAG_Y_CB_CR_SUBSAMPLING

Constant specifying the "YCbCrSubsampling" tag.

static int

TAG_Y_POSITION

Constant specifying the "YPosition" tag.

static int

TAG_Y_RESOLUTION

Constant specifying the "YResolution" tag.

static int

THRESHHOLDING_NONE

A value to be used with the "Thresholding" tag.

static int

THRESHHOLDING_ORDERED_DITHER

A value to be used with the "Thresholding" tag.

static int

THRESHHOLDING_RANDOMIZED_DITHER

A value to be used with the "Thresholding" tag.

static int

Y_CB_CR_POSITIONING_CENTERED

A value to be used with the "YCbCrPositioning" tag.

static int

Y_CB_CR_POSITIONING_COSITED

A value to be used with the "YCbCrPositioning" tag.

---

#### Field Summary

A value to be used with the "Compression" tag.

A value to be used with the "ExtraSamples" tag.

A value to be used with the "FillOrder" tag.

A value to be used with the "GrayResponseUnit" tag.

A value to be used with the "InkSet" tag.

A value to be used with the "JPEGProc" tag.

A mask to be used with the "NewSubfileType" tag.

A value to be used with the "Orientation" tag.

A value to be used with the "PhotometricInterpretation" tag.

A value to be used with the "PlanarConfiguration" tag.

A value to be used with the "Predictor" tag.

A value to be used with the "ResolutionUnit" tag.

A value to be used with the "SampleFormat" tag.

A value to be used with the "SubfileType" tag.

A mask to be used with the "T4Options" tag.

A mask to be used with the "T6Options" tag.

Constant specifying the "Artist" tag.

Constant specifying the "BitsPerSample" tag.

Constant specifying the "cell_length" tag.

Constant specifying the "Cell_Width" tag.

Constant specifying the "ColorMap" tag.

Constant specifying the "Compression" tag.

Constant specifying the "Copyright" tag.

Constant specifying the "DateTime" tag.

Constant specifying the "document_name" tag.

Constant specifying the "DotRange" tag.

Constant specifying the "ExtraSamples" tag.

Constant specifying the "fill_order" tag.

Constant specifying the "FreeByteCounts" tag.

Constant specifying the "FreeOffsets" tag.

Constant specifying the "GrayResponseCurve" tag.

Constant specifying the "GrayResponseUnit" tag.

Constant specifying the "HalftoneHints" tag.

Constant specifying the "HostComputer" tag.

Constant specifying the "ICC Profile" tag.

Constant specifying the "Image_description" tag.

Constant specifying the "ImageLength" tag.

Constant specifying the "ImageWidth" tag.

Constant specifying the "InkNames" tag.

Constant specifying the "InkSet" tag.

Constant specifying the "JPEGACTables" tag.

Constant specifying the "JPEGDCTables" tag.

Constant specifying the "JPEGInterchangeFormat" tag.

Constant specifying the "JPEGInterchangeFormatLength" tag.

Constant specifying the "JPEGLosslessPredictors" tag.

Constant specifying the "JPEGPointTransforms" tag.

Constant specifying the "JPEGProc" tag.

Constant specifying the "JPEGQTables" tag.

Constant specifying the "JPEGRestartInterval" tag.

Constant specifying the "JPEGTables" tag.

Constant specifying the "Make" tag.

Constant specifying the "Max_sample_value" tag.

Constant specifying the "Min_sample_value" tag.

Constant specifying the "Model" tag.

Constant specifying the "NewSubfileType" tag.

Constant specifying the "NumberOfInks" tag.

Constant specifying the "Orientation" tag.

Constant specifying the "PageName" tag.

Constant specifying the "PageNumber" tag.

Constant specifying the "PhotometricInterpretation" tag.

Constant specifying the "PlanarConfiguration" tag.

Constant specifying the "Predictor" tag.

Constant specifying the "PrimaryChromaticites" tag.

Constant specifying the "ReferenceBlackWhite" tag.

Constant specifying the "ResolutionUnit" tag.

Constant specifying the "Rows_per_strip" tag.

Constant specifying the "SMaxSampleValue" tag.

Constant specifying the "SMinSampleValue" tag.

Constant specifying the "SampleFormat" tag.

Constant specifying the "Samples_per_pixel" tag.

Constant specifying the "Software" tag.

Constant specifying the "Strip_byte_counts" tag.

Constant specifying the "Strip_offsets" tag.

Constant specifying the "SubfileType" tag.

Constant specifying the "T4Options" tag.

Constant specifying the "T6Options" tag.

Constant specifying the "TargetPrinter" tag.

Constant specifying the "Threshholding" tag.

Constant specifying the "TileByteCounts" tag.

Constant specifying the "TileLength" tag.

Constant specifying the "TileOffsets" tag.

Constant specifying the "TileWidth" tag.

Constant specifying the "TransferFunction" tag.

Constant specifying the "TransferRange" tag.

Constant specifying the "WhitePoint" tag.

Constant specifying the "XPosition" tag.

Constant specifying the "XResolution" tag.

Constant specifying the "YCbCrCoefficients" tag.

Constant specifying the "YCbCrPositioning" tag.

Constant specifying the "YCbCrSubsampling" tag.

Constant specifying the "YPosition" tag.

Constant specifying the "YResolution" tag.

A value to be used with the "Thresholding" tag.

A value to be used with the "YCbCrPositioning" tag.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

BaselineTIFFTagSet

getInstance

()

Returns a shared instance of a

BaselineTIFFTagSet

.

- Methods declared in class javax.imageio.plugins.tiff.

TIFFTagSet

getTag

,

getTag

,

getTagNames

,

getTagNumbers

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

Returns a shared instance of a

BaselineTIFFTagSet

.

Methods declared in class javax.imageio.plugins.tiff.

TIFFTagSet

getTag

,

getTag

,

getTagNames

,

getTagNumbers

---

#### Methods declared in class javax.imageio.plugins.tiff. TIFFTagSet

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

============ FIELD DETAIL ===========

- Field Detail

- TAG_NEW_SUBFILE_TYPE

```java
public static final int TAG_NEW_SUBFILE_TYPE
```

Constant specifying the "NewSubfileType" tag.

**See Also:** NEW_SUBFILE_TYPE_REDUCED_RESOLUTION

,

NEW_SUBFILE_TYPE_SINGLE_PAGE

,

NEW_SUBFILE_TYPE_TRANSPARENCY

,

Constant Field Values

- NEW_SUBFILE_TYPE_REDUCED_RESOLUTION

```java
public static final int NEW_SUBFILE_TYPE_REDUCED_RESOLUTION
```

A mask to be used with the "NewSubfileType" tag.

**See Also:** TAG_NEW_SUBFILE_TYPE

,

Constant Field Values

- NEW_SUBFILE_TYPE_SINGLE_PAGE

```java
public static final int NEW_SUBFILE_TYPE_SINGLE_PAGE
```

A mask to be used with the "NewSubfileType" tag.

**See Also:** TAG_NEW_SUBFILE_TYPE

,

Constant Field Values

- NEW_SUBFILE_TYPE_TRANSPARENCY

```java
public static final int NEW_SUBFILE_TYPE_TRANSPARENCY
```

A mask to be used with the "NewSubfileType" tag.

**See Also:** TAG_NEW_SUBFILE_TYPE

,

Constant Field Values

- TAG_SUBFILE_TYPE

```java
public static final int TAG_SUBFILE_TYPE
```

Constant specifying the "SubfileType" tag.

**See Also:** SUBFILE_TYPE_FULL_RESOLUTION

,

SUBFILE_TYPE_REDUCED_RESOLUTION

,

SUBFILE_TYPE_SINGLE_PAGE

,

Constant Field Values

- SUBFILE_TYPE_FULL_RESOLUTION

```java
public static final int SUBFILE_TYPE_FULL_RESOLUTION
```

A value to be used with the "SubfileType" tag.

**See Also:** TAG_SUBFILE_TYPE

,

Constant Field Values

- SUBFILE_TYPE_REDUCED_RESOLUTION

```java
public static final int SUBFILE_TYPE_REDUCED_RESOLUTION
```

A value to be used with the "SubfileType" tag.

**See Also:** TAG_SUBFILE_TYPE

,

Constant Field Values

- SUBFILE_TYPE_SINGLE_PAGE

```java
public static final int SUBFILE_TYPE_SINGLE_PAGE
```

A value to be used with the "SubfileType" tag.

**See Also:** TAG_SUBFILE_TYPE

,

Constant Field Values

- TAG_IMAGE_WIDTH

```java
public static final int TAG_IMAGE_WIDTH
```

Constant specifying the "ImageWidth" tag.

**See Also:** Constant Field Values

- TAG_IMAGE_LENGTH

```java
public static final int TAG_IMAGE_LENGTH
```

Constant specifying the "ImageLength" tag.

**See Also:** Constant Field Values

- TAG_BITS_PER_SAMPLE

```java
public static final int TAG_BITS_PER_SAMPLE
```

Constant specifying the "BitsPerSample" tag.

**See Also:** Constant Field Values

- TAG_COMPRESSION

```java
public static final int TAG_COMPRESSION
```

Constant specifying the "Compression" tag.

**See Also:** COMPRESSION_NONE

,

COMPRESSION_CCITT_RLE

,

COMPRESSION_CCITT_T_4

,

COMPRESSION_CCITT_T_6

,

COMPRESSION_LZW

,

COMPRESSION_OLD_JPEG

,

COMPRESSION_JPEG

,

COMPRESSION_ZLIB

,

COMPRESSION_PACKBITS

,

COMPRESSION_DEFLATE

,

Constant Field Values

- COMPRESSION_NONE

```java
public static final int COMPRESSION_NONE
```

A value to be used with the "Compression" tag.

**See Also:** TAG_COMPRESSION

,

Constant Field Values

- COMPRESSION_CCITT_RLE

```java
public static final int COMPRESSION_CCITT_RLE
```

A value to be used with the "Compression" tag.

**See Also:** TAG_COMPRESSION

,

Constant Field Values

- COMPRESSION_CCITT_T_4

```java
public static final int COMPRESSION_CCITT_T_4
```

A value to be used with the "Compression" tag.

**See Also:** TAG_COMPRESSION

,

Constant Field Values

- COMPRESSION_CCITT_T_6

```java
public static final int COMPRESSION_CCITT_T_6
```

A value to be used with the "Compression" tag.

**See Also:** TAG_COMPRESSION

,

Constant Field Values

- COMPRESSION_LZW

```java
public static final int COMPRESSION_LZW
```

A value to be used with the "Compression" tag.

**See Also:** TAG_COMPRESSION

,

Constant Field Values

- COMPRESSION_OLD_JPEG

```java
public static final int COMPRESSION_OLD_JPEG
```

A value to be used with the "Compression" tag.

**See Also:** TAG_COMPRESSION

,

Constant Field Values

- COMPRESSION_JPEG

```java
public static final int COMPRESSION_JPEG
```

A value to be used with the "Compression" tag.

**See Also:** TAG_COMPRESSION

,

Constant Field Values

- COMPRESSION_ZLIB

```java
public static final int COMPRESSION_ZLIB
```

A value to be used with the "Compression" tag.

**See Also:** TAG_COMPRESSION

,

Constant Field Values

- COMPRESSION_PACKBITS

```java
public static final int COMPRESSION_PACKBITS
```

A value to be used with the "Compression" tag.

**See Also:** TAG_COMPRESSION

,

Constant Field Values

- COMPRESSION_DEFLATE

```java
public static final int COMPRESSION_DEFLATE
```

A value to be used with the "Compression" tag.

**See Also:** TAG_COMPRESSION

,

DEFLATE specification

,

Constant Field Values

- TAG_PHOTOMETRIC_INTERPRETATION

```java
public static final int TAG_PHOTOMETRIC_INTERPRETATION
```

Constant specifying the "PhotometricInterpretation" tag.

**See Also:** PHOTOMETRIC_INTERPRETATION_WHITE_IS_ZERO

,

PHOTOMETRIC_INTERPRETATION_BLACK_IS_ZERO

,

PHOTOMETRIC_INTERPRETATION_RGB

,

PHOTOMETRIC_INTERPRETATION_PALETTE_COLOR

,

PHOTOMETRIC_INTERPRETATION_TRANSPARENCY_MASK

,

PHOTOMETRIC_INTERPRETATION_Y_CB_CR

,

PHOTOMETRIC_INTERPRETATION_CIELAB

,

PHOTOMETRIC_INTERPRETATION_ICCLAB

,

Constant Field Values

- PHOTOMETRIC_INTERPRETATION_WHITE_IS_ZERO

```java
public static final int PHOTOMETRIC_INTERPRETATION_WHITE_IS_ZERO
```

A value to be used with the "PhotometricInterpretation" tag.

**See Also:** TAG_PHOTOMETRIC_INTERPRETATION

,

Constant Field Values

- PHOTOMETRIC_INTERPRETATION_BLACK_IS_ZERO

```java
public static final int PHOTOMETRIC_INTERPRETATION_BLACK_IS_ZERO
```

A value to be used with the "PhotometricInterpretation" tag.

**See Also:** TAG_PHOTOMETRIC_INTERPRETATION

,

Constant Field Values

- PHOTOMETRIC_INTERPRETATION_RGB

```java
public static final int PHOTOMETRIC_INTERPRETATION_RGB
```

A value to be used with the "PhotometricInterpretation" tag.

**See Also:** TAG_PHOTOMETRIC_INTERPRETATION

,

Constant Field Values

- PHOTOMETRIC_INTERPRETATION_PALETTE_COLOR

```java
public static final int PHOTOMETRIC_INTERPRETATION_PALETTE_COLOR
```

A value to be used with the "PhotometricInterpretation" tag.

**See Also:** TAG_PHOTOMETRIC_INTERPRETATION

,

Constant Field Values

- PHOTOMETRIC_INTERPRETATION_TRANSPARENCY_MASK

```java
public static final int PHOTOMETRIC_INTERPRETATION_TRANSPARENCY_MASK
```

A value to be used with the "PhotometricInterpretation" tag.

**See Also:** TAG_PHOTOMETRIC_INTERPRETATION

,

Constant Field Values

- PHOTOMETRIC_INTERPRETATION_CMYK

```java
public static final int PHOTOMETRIC_INTERPRETATION_CMYK
```

A value to be used with the "PhotometricInterpretation" tag.

**See Also:** TAG_PHOTOMETRIC_INTERPRETATION

,

Constant Field Values

- PHOTOMETRIC_INTERPRETATION_Y_CB_CR

```java
public static final int PHOTOMETRIC_INTERPRETATION_Y_CB_CR
```

A value to be used with the "PhotometricInterpretation" tag.

**See Also:** TAG_PHOTOMETRIC_INTERPRETATION

,

Constant Field Values

- PHOTOMETRIC_INTERPRETATION_CIELAB

```java
public static final int PHOTOMETRIC_INTERPRETATION_CIELAB
```

A value to be used with the "PhotometricInterpretation" tag.

**See Also:** TAG_PHOTOMETRIC_INTERPRETATION

,

Constant Field Values

- PHOTOMETRIC_INTERPRETATION_ICCLAB

```java
public static final int PHOTOMETRIC_INTERPRETATION_ICCLAB
```

A value to be used with the "PhotometricInterpretation" tag.

**See Also:** TAG_PHOTOMETRIC_INTERPRETATION

,

Constant Field Values

- TAG_THRESHHOLDING

```java
public static final int TAG_THRESHHOLDING
```

Constant specifying the "Threshholding" tag.

**See Also:** THRESHHOLDING_NONE

,

THRESHHOLDING_ORDERED_DITHER

,

THRESHHOLDING_RANDOMIZED_DITHER

,

Constant Field Values

- THRESHHOLDING_NONE

```java
public static final int THRESHHOLDING_NONE
```

A value to be used with the "Thresholding" tag.

**See Also:** TAG_THRESHHOLDING

,

Constant Field Values

- THRESHHOLDING_ORDERED_DITHER

```java
public static final int THRESHHOLDING_ORDERED_DITHER
```

A value to be used with the "Thresholding" tag.

**See Also:** TAG_THRESHHOLDING

,

Constant Field Values

- THRESHHOLDING_RANDOMIZED_DITHER

```java
public static final int THRESHHOLDING_RANDOMIZED_DITHER
```

A value to be used with the "Thresholding" tag.

**See Also:** TAG_THRESHHOLDING

,

Constant Field Values

- TAG_CELL_WIDTH

```java
public static final int TAG_CELL_WIDTH
```

Constant specifying the "Cell_Width" tag.

**See Also:** Constant Field Values

- TAG_CELL_LENGTH

```java
public static final int TAG_CELL_LENGTH
```

Constant specifying the "cell_length" tag.

**See Also:** Constant Field Values

- TAG_FILL_ORDER

```java
public static final int TAG_FILL_ORDER
```

Constant specifying the "fill_order" tag.

**See Also:** FILL_ORDER_LEFT_TO_RIGHT

,

FILL_ORDER_RIGHT_TO_LEFT

,

Constant Field Values

- FILL_ORDER_LEFT_TO_RIGHT

```java
public static final int FILL_ORDER_LEFT_TO_RIGHT
```

A value to be used with the "FillOrder" tag.

**See Also:** TAG_FILL_ORDER

,

Constant Field Values

- FILL_ORDER_RIGHT_TO_LEFT

```java
public static final int FILL_ORDER_RIGHT_TO_LEFT
```

A value to be used with the "FillOrder" tag.

**See Also:** TAG_FILL_ORDER

,

Constant Field Values

- TAG_DOCUMENT_NAME

```java
public static final int TAG_DOCUMENT_NAME
```

Constant specifying the "document_name" tag.

**See Also:** Constant Field Values

- TAG_IMAGE_DESCRIPTION

```java
public static final int TAG_IMAGE_DESCRIPTION
```

Constant specifying the "Image_description" tag.

**See Also:** Constant Field Values

- TAG_MAKE

```java
public static final int TAG_MAKE
```

Constant specifying the "Make" tag.

**See Also:** Constant Field Values

- TAG_MODEL

```java
public static final int TAG_MODEL
```

Constant specifying the "Model" tag.

**See Also:** Constant Field Values

- TAG_STRIP_OFFSETS

```java
public static final int TAG_STRIP_OFFSETS
```

Constant specifying the "Strip_offsets" tag.

**See Also:** Constant Field Values

- TAG_ORIENTATION

```java
public static final int TAG_ORIENTATION
```

Constant specifying the "Orientation" tag.

**See Also:** ORIENTATION_ROW_0_TOP_COLUMN_0_LEFT

,

ORIENTATION_ROW_0_TOP_COLUMN_0_RIGHT

,

ORIENTATION_ROW_0_BOTTOM_COLUMN_0_RIGHT

,

ORIENTATION_ROW_0_BOTTOM_COLUMN_0_LEFT

,

ORIENTATION_ROW_0_LEFT_COLUMN_0_TOP

,

ORIENTATION_ROW_0_RIGHT_COLUMN_0_TOP

,

ORIENTATION_ROW_0_RIGHT_COLUMN_0_BOTTOM

,

ORIENTATION_ROW_0_LEFT_COLUMN_0_BOTTOM

,

Constant Field Values

- ORIENTATION_ROW_0_TOP_COLUMN_0_LEFT

```java
public static final int ORIENTATION_ROW_0_TOP_COLUMN_0_LEFT
```

A value to be used with the "Orientation" tag.

**See Also:** TAG_ORIENTATION

,

Constant Field Values

- ORIENTATION_ROW_0_TOP_COLUMN_0_RIGHT

```java
public static final int ORIENTATION_ROW_0_TOP_COLUMN_0_RIGHT
```

A value to be used with the "Orientation" tag.

**See Also:** TAG_ORIENTATION

,

Constant Field Values

- ORIENTATION_ROW_0_BOTTOM_COLUMN_0_RIGHT

```java
public static final int ORIENTATION_ROW_0_BOTTOM_COLUMN_0_RIGHT
```

A value to be used with the "Orientation" tag.

**See Also:** TAG_ORIENTATION

,

Constant Field Values

- ORIENTATION_ROW_0_BOTTOM_COLUMN_0_LEFT

```java
public static final int ORIENTATION_ROW_0_BOTTOM_COLUMN_0_LEFT
```

A value to be used with the "Orientation" tag.

**See Also:** TAG_ORIENTATION

,

Constant Field Values

- ORIENTATION_ROW_0_LEFT_COLUMN_0_TOP

```java
public static final int ORIENTATION_ROW_0_LEFT_COLUMN_0_TOP
```

A value to be used with the "Orientation" tag.

**See Also:** TAG_ORIENTATION

,

Constant Field Values

- ORIENTATION_ROW_0_RIGHT_COLUMN_0_TOP

```java
public static final int ORIENTATION_ROW_0_RIGHT_COLUMN_0_TOP
```

A value to be used with the "Orientation" tag.

**See Also:** TAG_ORIENTATION

,

Constant Field Values

- ORIENTATION_ROW_0_RIGHT_COLUMN_0_BOTTOM

```java
public static final int ORIENTATION_ROW_0_RIGHT_COLUMN_0_BOTTOM
```

A value to be used with the "Orientation" tag.

**See Also:** TAG_ORIENTATION

,

Constant Field Values

- ORIENTATION_ROW_0_LEFT_COLUMN_0_BOTTOM

```java
public static final int ORIENTATION_ROW_0_LEFT_COLUMN_0_BOTTOM
```

A value to be used with the "Orientation" tag.

**See Also:** TAG_ORIENTATION

,

Constant Field Values

- TAG_SAMPLES_PER_PIXEL

```java
public static final int TAG_SAMPLES_PER_PIXEL
```

Constant specifying the "Samples_per_pixel" tag.

**See Also:** Constant Field Values

- TAG_ROWS_PER_STRIP

```java
public static final int TAG_ROWS_PER_STRIP
```

Constant specifying the "Rows_per_strip" tag.

**See Also:** Constant Field Values

- TAG_STRIP_BYTE_COUNTS

```java
public static final int TAG_STRIP_BYTE_COUNTS
```

Constant specifying the "Strip_byte_counts" tag.

**See Also:** Constant Field Values

- TAG_MIN_SAMPLE_VALUE

```java
public static final int TAG_MIN_SAMPLE_VALUE
```

Constant specifying the "Min_sample_value" tag.

**See Also:** Constant Field Values

- TAG_MAX_SAMPLE_VALUE

```java
public static final int TAG_MAX_SAMPLE_VALUE
```

Constant specifying the "Max_sample_value" tag.

**See Also:** Constant Field Values

- TAG_X_RESOLUTION

```java
public static final int TAG_X_RESOLUTION
```

Constant specifying the "XResolution" tag.

**See Also:** Constant Field Values

- TAG_Y_RESOLUTION

```java
public static final int TAG_Y_RESOLUTION
```

Constant specifying the "YResolution" tag.

**See Also:** Constant Field Values

- TAG_PLANAR_CONFIGURATION

```java
public static final int TAG_PLANAR_CONFIGURATION
```

Constant specifying the "PlanarConfiguration" tag.

**See Also:** PLANAR_CONFIGURATION_CHUNKY

,

PLANAR_CONFIGURATION_PLANAR

,

Constant Field Values

- PLANAR_CONFIGURATION_CHUNKY

```java
public static final int PLANAR_CONFIGURATION_CHUNKY
```

A value to be used with the "PlanarConfiguration" tag.

**See Also:** TAG_PLANAR_CONFIGURATION

,

Constant Field Values

- PLANAR_CONFIGURATION_PLANAR

```java
public static final int PLANAR_CONFIGURATION_PLANAR
```

A value to be used with the "PlanarConfiguration" tag.

**See Also:** TAG_PLANAR_CONFIGURATION

,

Constant Field Values

- TAG_PAGE_NAME

```java
public static final int TAG_PAGE_NAME
```

Constant specifying the "PageName" tag.

**See Also:** Constant Field Values

- TAG_X_POSITION

```java
public static final int TAG_X_POSITION
```

Constant specifying the "XPosition" tag.

**See Also:** Constant Field Values

- TAG_Y_POSITION

```java
public static final int TAG_Y_POSITION
```

Constant specifying the "YPosition" tag.

**See Also:** Constant Field Values

- TAG_FREE_OFFSETS

```java
public static final int TAG_FREE_OFFSETS
```

Constant specifying the "FreeOffsets" tag.

**See Also:** Constant Field Values

- TAG_FREE_BYTE_COUNTS

```java
public static final int TAG_FREE_BYTE_COUNTS
```

Constant specifying the "FreeByteCounts" tag.

**See Also:** Constant Field Values

- TAG_GRAY_RESPONSE_UNIT

```java
public static final int TAG_GRAY_RESPONSE_UNIT
```

Constant specifying the "GrayResponseUnit" tag.

**See Also:** GRAY_RESPONSE_UNIT_TENTHS

,

GRAY_RESPONSE_UNIT_HUNDREDTHS

,

GRAY_RESPONSE_UNIT_THOUSANDTHS

,

GRAY_RESPONSE_UNIT_TEN_THOUSANDTHS

,

GRAY_RESPONSE_UNIT_HUNDRED_THOUSANDTHS

,

Constant Field Values

- GRAY_RESPONSE_UNIT_TENTHS

```java
public static final int GRAY_RESPONSE_UNIT_TENTHS
```

A value to be used with the "GrayResponseUnit" tag.

**See Also:** TAG_GRAY_RESPONSE_UNIT

,

Constant Field Values

- GRAY_RESPONSE_UNIT_HUNDREDTHS

```java
public static final int GRAY_RESPONSE_UNIT_HUNDREDTHS
```

A value to be used with the "GrayResponseUnit" tag.

**See Also:** TAG_GRAY_RESPONSE_UNIT

,

Constant Field Values

- GRAY_RESPONSE_UNIT_THOUSANDTHS

```java
public static final int GRAY_RESPONSE_UNIT_THOUSANDTHS
```

A value to be used with the "GrayResponseUnit" tag.

**See Also:** TAG_GRAY_RESPONSE_UNIT

,

Constant Field Values

- GRAY_RESPONSE_UNIT_TEN_THOUSANDTHS

```java
public static final int GRAY_RESPONSE_UNIT_TEN_THOUSANDTHS
```

A value to be used with the "GrayResponseUnit" tag.

**See Also:** TAG_GRAY_RESPONSE_UNIT

,

Constant Field Values

- GRAY_RESPONSE_UNIT_HUNDRED_THOUSANDTHS

```java
public static final int GRAY_RESPONSE_UNIT_HUNDRED_THOUSANDTHS
```

A value to be used with the "GrayResponseUnit" tag.

**See Also:** TAG_GRAY_RESPONSE_UNIT

,

Constant Field Values

- TAG_GRAY_RESPONSE_CURVE

```java
public static final int TAG_GRAY_RESPONSE_CURVE
```

Constant specifying the "GrayResponseCurve" tag.

**See Also:** Constant Field Values

- TAG_T4_OPTIONS

```java
public static final int TAG_T4_OPTIONS
```

Constant specifying the "T4Options" tag.

**See Also:** T4_OPTIONS_2D_CODING

,

T4_OPTIONS_UNCOMPRESSED

,

T4_OPTIONS_EOL_BYTE_ALIGNED

,

Constant Field Values

- T4_OPTIONS_2D_CODING

```java
public static final int T4_OPTIONS_2D_CODING
```

A mask to be used with the "T4Options" tag.

**See Also:** TAG_T4_OPTIONS

,

Constant Field Values

- T4_OPTIONS_UNCOMPRESSED

```java
public static final int T4_OPTIONS_UNCOMPRESSED
```

A mask to be used with the "T4Options" tag.

**See Also:** TAG_T4_OPTIONS

,

Constant Field Values

- T4_OPTIONS_EOL_BYTE_ALIGNED

```java
public static final int T4_OPTIONS_EOL_BYTE_ALIGNED
```

A mask to be used with the "T4Options" tag.

**See Also:** TAG_T4_OPTIONS

,

Constant Field Values

- TAG_T6_OPTIONS

```java
public static final int TAG_T6_OPTIONS
```

Constant specifying the "T6Options" tag.

**See Also:** T6_OPTIONS_UNCOMPRESSED

,

Constant Field Values

- T6_OPTIONS_UNCOMPRESSED

```java
public static final int T6_OPTIONS_UNCOMPRESSED
```

A mask to be used with the "T6Options" tag.

**See Also:** TAG_T6_OPTIONS

,

Constant Field Values

- TAG_RESOLUTION_UNIT

```java
public static final int TAG_RESOLUTION_UNIT
```

Constant specifying the "ResolutionUnit" tag.

**See Also:** RESOLUTION_UNIT_NONE

,

RESOLUTION_UNIT_INCH

,

RESOLUTION_UNIT_CENTIMETER

,

Constant Field Values

- RESOLUTION_UNIT_NONE

```java
public static final int RESOLUTION_UNIT_NONE
```

A value to be used with the "ResolutionUnit" tag.

**See Also:** TAG_RESOLUTION_UNIT

,

Constant Field Values

- RESOLUTION_UNIT_INCH

```java
public static final int RESOLUTION_UNIT_INCH
```

A value to be used with the "ResolutionUnit" tag.

**See Also:** TAG_RESOLUTION_UNIT

,

Constant Field Values

- RESOLUTION_UNIT_CENTIMETER

```java
public static final int RESOLUTION_UNIT_CENTIMETER
```

A value to be used with the "ResolutionUnit" tag.

**See Also:** TAG_RESOLUTION_UNIT

,

Constant Field Values

- TAG_PAGE_NUMBER

```java
public static final int TAG_PAGE_NUMBER
```

Constant specifying the "PageNumber" tag.

**See Also:** Constant Field Values

- TAG_TRANSFER_FUNCTION

```java
public static final int TAG_TRANSFER_FUNCTION
```

Constant specifying the "TransferFunction" tag.

**See Also:** Constant Field Values

- TAG_SOFTWARE

```java
public static final int TAG_SOFTWARE
```

Constant specifying the "Software" tag.

**See Also:** Constant Field Values

- TAG_DATE_TIME

```java
public static final int TAG_DATE_TIME
```

Constant specifying the "DateTime" tag.

**See Also:** Constant Field Values

- TAG_ARTIST

```java
public static final int TAG_ARTIST
```

Constant specifying the "Artist" tag.

**See Also:** Constant Field Values

- TAG_HOST_COMPUTER

```java
public static final int TAG_HOST_COMPUTER
```

Constant specifying the "HostComputer" tag.

**See Also:** Constant Field Values

- TAG_PREDICTOR

```java
public static final int TAG_PREDICTOR
```

Constant specifying the "Predictor" tag.

**See Also:** TAG_WHITE_POINT

,

TAG_PRIMARY_CHROMATICITES

,

TAG_COLOR_MAP

,

TAG_HALFTONE_HINTS

,

TAG_TILE_WIDTH

,

TAG_TILE_LENGTH

,

TAG_TILE_OFFSETS

,

TAG_TILE_BYTE_COUNTS

,

Constant Field Values

- PREDICTOR_NONE

```java
public static final int PREDICTOR_NONE
```

A value to be used with the "Predictor" tag.

**See Also:** TAG_PREDICTOR

,

Constant Field Values

- PREDICTOR_HORIZONTAL_DIFFERENCING

```java
public static final int PREDICTOR_HORIZONTAL_DIFFERENCING
```

A value to be used with the "Predictor" tag.

**See Also:** TAG_PREDICTOR

,

Constant Field Values

- TAG_WHITE_POINT

```java
public static final int TAG_WHITE_POINT
```

Constant specifying the "WhitePoint" tag.

**See Also:** Constant Field Values

- TAG_PRIMARY_CHROMATICITES

```java
public static final int TAG_PRIMARY_CHROMATICITES
```

Constant specifying the "PrimaryChromaticites" tag.

**See Also:** Constant Field Values

- TAG_COLOR_MAP

```java
public static final int TAG_COLOR_MAP
```

Constant specifying the "ColorMap" tag.

**See Also:** Constant Field Values

- TAG_HALFTONE_HINTS

```java
public static final int TAG_HALFTONE_HINTS
```

Constant specifying the "HalftoneHints" tag.

**See Also:** Constant Field Values

- TAG_TILE_WIDTH

```java
public static final int TAG_TILE_WIDTH
```

Constant specifying the "TileWidth" tag.

**See Also:** Constant Field Values

- TAG_TILE_LENGTH

```java
public static final int TAG_TILE_LENGTH
```

Constant specifying the "TileLength" tag.

**See Also:** Constant Field Values

- TAG_TILE_OFFSETS

```java
public static final int TAG_TILE_OFFSETS
```

Constant specifying the "TileOffsets" tag.

**See Also:** Constant Field Values

- TAG_TILE_BYTE_COUNTS

```java
public static final int TAG_TILE_BYTE_COUNTS
```

Constant specifying the "TileByteCounts" tag.

**See Also:** Constant Field Values

- TAG_INK_SET

```java
public static final int TAG_INK_SET
```

Constant specifying the "InkSet" tag.

**See Also:** INK_SET_CMYK

,

INK_SET_NOT_CMYK

,

Constant Field Values

- INK_SET_CMYK

```java
public static final int INK_SET_CMYK
```

A value to be used with the "InkSet" tag.

**See Also:** TAG_INK_SET

,

Constant Field Values

- INK_SET_NOT_CMYK

```java
public static final int INK_SET_NOT_CMYK
```

A value to be used with the "InkSet" tag.

**See Also:** TAG_INK_SET

,

Constant Field Values

- TAG_INK_NAMES

```java
public static final int TAG_INK_NAMES
```

Constant specifying the "InkNames" tag.

**See Also:** Constant Field Values

- TAG_NUMBER_OF_INKS

```java
public static final int TAG_NUMBER_OF_INKS
```

Constant specifying the "NumberOfInks" tag.

**See Also:** Constant Field Values

- TAG_DOT_RANGE

```java
public static final int TAG_DOT_RANGE
```

Constant specifying the "DotRange" tag.

**See Also:** Constant Field Values

- TAG_TARGET_PRINTER

```java
public static final int TAG_TARGET_PRINTER
```

Constant specifying the "TargetPrinter" tag.

**See Also:** Constant Field Values

- TAG_EXTRA_SAMPLES

```java
public static final int TAG_EXTRA_SAMPLES
```

Constant specifying the "ExtraSamples" tag.

**See Also:** EXTRA_SAMPLES_UNSPECIFIED

,

EXTRA_SAMPLES_ASSOCIATED_ALPHA

,

EXTRA_SAMPLES_UNASSOCIATED_ALPHA

,

Constant Field Values

- EXTRA_SAMPLES_UNSPECIFIED

```java
public static final int EXTRA_SAMPLES_UNSPECIFIED
```

A value to be used with the "ExtraSamples" tag.

**See Also:** TAG_EXTRA_SAMPLES

,

Constant Field Values

- EXTRA_SAMPLES_ASSOCIATED_ALPHA

```java
public static final int EXTRA_SAMPLES_ASSOCIATED_ALPHA
```

A value to be used with the "ExtraSamples" tag.

**See Also:** TAG_EXTRA_SAMPLES

,

Constant Field Values

- EXTRA_SAMPLES_UNASSOCIATED_ALPHA

```java
public static final int EXTRA_SAMPLES_UNASSOCIATED_ALPHA
```

A value to be used with the "ExtraSamples" tag.

**See Also:** TAG_EXTRA_SAMPLES

,

Constant Field Values

- TAG_SAMPLE_FORMAT

```java
public static final int TAG_SAMPLE_FORMAT
```

Constant specifying the "SampleFormat" tag.

**See Also:** SAMPLE_FORMAT_UNSIGNED_INTEGER

,

SAMPLE_FORMAT_SIGNED_INTEGER

,

SAMPLE_FORMAT_FLOATING_POINT

,

SAMPLE_FORMAT_UNDEFINED

,

Constant Field Values

- SAMPLE_FORMAT_UNSIGNED_INTEGER

```java
public static final int SAMPLE_FORMAT_UNSIGNED_INTEGER
```

A value to be used with the "SampleFormat" tag.

**See Also:** TAG_SAMPLE_FORMAT

,

Constant Field Values

- SAMPLE_FORMAT_SIGNED_INTEGER

```java
public static final int SAMPLE_FORMAT_SIGNED_INTEGER
```

A value to be used with the "SampleFormat" tag.

**See Also:** TAG_SAMPLE_FORMAT

,

Constant Field Values

- SAMPLE_FORMAT_FLOATING_POINT

```java
public static final int SAMPLE_FORMAT_FLOATING_POINT
```

A value to be used with the "SampleFormat" tag.

**See Also:** TAG_SAMPLE_FORMAT

,

Constant Field Values

- SAMPLE_FORMAT_UNDEFINED

```java
public static final int SAMPLE_FORMAT_UNDEFINED
```

A value to be used with the "SampleFormat" tag.

**See Also:** TAG_SAMPLE_FORMAT

,

Constant Field Values

- TAG_S_MIN_SAMPLE_VALUE

```java
public static final int TAG_S_MIN_SAMPLE_VALUE
```

Constant specifying the "SMinSampleValue" tag.

**See Also:** Constant Field Values

- TAG_S_MAX_SAMPLE_VALUE

```java
public static final int TAG_S_MAX_SAMPLE_VALUE
```

Constant specifying the "SMaxSampleValue" tag.

**See Also:** Constant Field Values

- TAG_TRANSFER_RANGE

```java
public static final int TAG_TRANSFER_RANGE
```

Constant specifying the "TransferRange" tag.

**See Also:** Constant Field Values

- TAG_JPEG_TABLES

```java
public static final int TAG_JPEG_TABLES
```

Constant specifying the "JPEGTables" tag.

**See Also:** JPEG-in-TIFF compression

,

Constant Field Values

- TAG_JPEG_PROC

```java
public static final int TAG_JPEG_PROC
```

Constant specifying the "JPEGProc" tag.

**See Also:** Constant Field Values

- JPEG_PROC_BASELINE

```java
public static final int JPEG_PROC_BASELINE
```

A value to be used with the "JPEGProc" tag.

**See Also:** TAG_JPEG_PROC

,

Constant Field Values

- JPEG_PROC_LOSSLESS

```java
public static final int JPEG_PROC_LOSSLESS
```

A value to be used with the "JPEGProc" tag.

**See Also:** TAG_JPEG_PROC

,

Constant Field Values

- TAG_JPEG_INTERCHANGE_FORMAT

```java
public static final int TAG_JPEG_INTERCHANGE_FORMAT
```

Constant specifying the "JPEGInterchangeFormat" tag.

**See Also:** Constant Field Values

- TAG_JPEG_INTERCHANGE_FORMAT_LENGTH

```java
public static final int TAG_JPEG_INTERCHANGE_FORMAT_LENGTH
```

Constant specifying the "JPEGInterchangeFormatLength" tag.

**See Also:** Constant Field Values

- TAG_JPEG_RESTART_INTERVAL

```java
public static final int TAG_JPEG_RESTART_INTERVAL
```

Constant specifying the "JPEGRestartInterval" tag.

**See Also:** Constant Field Values

- TAG_JPEG_LOSSLESS_PREDICTORS

```java
public static final int TAG_JPEG_LOSSLESS_PREDICTORS
```

Constant specifying the "JPEGLosslessPredictors" tag.

**See Also:** Constant Field Values

- TAG_JPEG_POINT_TRANSFORMS

```java
public static final int TAG_JPEG_POINT_TRANSFORMS
```

Constant specifying the "JPEGPointTransforms" tag.

**See Also:** Constant Field Values

- TAG_JPEG_Q_TABLES

```java
public static final int TAG_JPEG_Q_TABLES
```

Constant specifying the "JPEGQTables" tag.

**See Also:** Constant Field Values

- TAG_JPEG_DC_TABLES

```java
public static final int TAG_JPEG_DC_TABLES
```

Constant specifying the "JPEGDCTables" tag.

**See Also:** Constant Field Values

- TAG_JPEG_AC_TABLES

```java
public static final int TAG_JPEG_AC_TABLES
```

Constant specifying the "JPEGACTables" tag.

**See Also:** Constant Field Values

- TAG_Y_CB_CR_COEFFICIENTS

```java
public static final int TAG_Y_CB_CR_COEFFICIENTS
```

Constant specifying the "YCbCrCoefficients" tag.

**See Also:** Constant Field Values

- TAG_Y_CB_CR_SUBSAMPLING

```java
public static final int TAG_Y_CB_CR_SUBSAMPLING
```

Constant specifying the "YCbCrSubsampling" tag.

**See Also:** Constant Field Values

- TAG_Y_CB_CR_POSITIONING

```java
public static final int TAG_Y_CB_CR_POSITIONING
```

Constant specifying the "YCbCrPositioning" tag.

**See Also:** Y_CB_CR_POSITIONING_CENTERED

,

Y_CB_CR_POSITIONING_COSITED

,

Constant Field Values

- Y_CB_CR_POSITIONING_CENTERED

```java
public static final int Y_CB_CR_POSITIONING_CENTERED
```

A value to be used with the "YCbCrPositioning" tag.

**See Also:** TAG_Y_CB_CR_POSITIONING

,

Constant Field Values

- Y_CB_CR_POSITIONING_COSITED

```java
public static final int Y_CB_CR_POSITIONING_COSITED
```

A value to be used with the "YCbCrPositioning" tag.

**See Also:** TAG_Y_CB_CR_POSITIONING

,

Constant Field Values

- TAG_REFERENCE_BLACK_WHITE

```java
public static final int TAG_REFERENCE_BLACK_WHITE
```

Constant specifying the "ReferenceBlackWhite" tag.

**See Also:** Constant Field Values

- TAG_COPYRIGHT

```java
public static final int TAG_COPYRIGHT
```

Constant specifying the "Copyright" tag.

**See Also:** Constant Field Values

- TAG_ICC_PROFILE

```java
public static final int TAG_ICC_PROFILE
```

Constant specifying the "ICC Profile" tag.

**See Also:** ICC Specification, section B.4: Embedding ICC profiles in TIFF files

,

Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getInstance

```java
public static
BaselineTIFFTagSet
getInstance()
```

Returns a shared instance of a

BaselineTIFFTagSet

.

**Returns:** a

BaselineTIFFTagSet

instance.

Field Detail

- TAG_NEW_SUBFILE_TYPE

```java
public static final int TAG_NEW_SUBFILE_TYPE
```

Constant specifying the "NewSubfileType" tag.

**See Also:** NEW_SUBFILE_TYPE_REDUCED_RESOLUTION

,

NEW_SUBFILE_TYPE_SINGLE_PAGE

,

NEW_SUBFILE_TYPE_TRANSPARENCY

,

Constant Field Values

- NEW_SUBFILE_TYPE_REDUCED_RESOLUTION

```java
public static final int NEW_SUBFILE_TYPE_REDUCED_RESOLUTION
```

A mask to be used with the "NewSubfileType" tag.

**See Also:** TAG_NEW_SUBFILE_TYPE

,

Constant Field Values

- NEW_SUBFILE_TYPE_SINGLE_PAGE

```java
public static final int NEW_SUBFILE_TYPE_SINGLE_PAGE
```

A mask to be used with the "NewSubfileType" tag.

**See Also:** TAG_NEW_SUBFILE_TYPE

,

Constant Field Values

- NEW_SUBFILE_TYPE_TRANSPARENCY

```java
public static final int NEW_SUBFILE_TYPE_TRANSPARENCY
```

A mask to be used with the "NewSubfileType" tag.

**See Also:** TAG_NEW_SUBFILE_TYPE

,

Constant Field Values

- TAG_SUBFILE_TYPE

```java
public static final int TAG_SUBFILE_TYPE
```

Constant specifying the "SubfileType" tag.

**See Also:** SUBFILE_TYPE_FULL_RESOLUTION

,

SUBFILE_TYPE_REDUCED_RESOLUTION

,

SUBFILE_TYPE_SINGLE_PAGE

,

Constant Field Values

- SUBFILE_TYPE_FULL_RESOLUTION

```java
public static final int SUBFILE_TYPE_FULL_RESOLUTION
```

A value to be used with the "SubfileType" tag.

**See Also:** TAG_SUBFILE_TYPE

,

Constant Field Values

- SUBFILE_TYPE_REDUCED_RESOLUTION

```java
public static final int SUBFILE_TYPE_REDUCED_RESOLUTION
```

A value to be used with the "SubfileType" tag.

**See Also:** TAG_SUBFILE_TYPE

,

Constant Field Values

- SUBFILE_TYPE_SINGLE_PAGE

```java
public static final int SUBFILE_TYPE_SINGLE_PAGE
```

A value to be used with the "SubfileType" tag.

**See Also:** TAG_SUBFILE_TYPE

,

Constant Field Values

- TAG_IMAGE_WIDTH

```java
public static final int TAG_IMAGE_WIDTH
```

Constant specifying the "ImageWidth" tag.

**See Also:** Constant Field Values

- TAG_IMAGE_LENGTH

```java
public static final int TAG_IMAGE_LENGTH
```

Constant specifying the "ImageLength" tag.

**See Also:** Constant Field Values

- TAG_BITS_PER_SAMPLE

```java
public static final int TAG_BITS_PER_SAMPLE
```

Constant specifying the "BitsPerSample" tag.

**See Also:** Constant Field Values

- TAG_COMPRESSION

```java
public static final int TAG_COMPRESSION
```

Constant specifying the "Compression" tag.

**See Also:** COMPRESSION_NONE

,

COMPRESSION_CCITT_RLE

,

COMPRESSION_CCITT_T_4

,

COMPRESSION_CCITT_T_6

,

COMPRESSION_LZW

,

COMPRESSION_OLD_JPEG

,

COMPRESSION_JPEG

,

COMPRESSION_ZLIB

,

COMPRESSION_PACKBITS

,

COMPRESSION_DEFLATE

,

Constant Field Values

- COMPRESSION_NONE

```java
public static final int COMPRESSION_NONE
```

A value to be used with the "Compression" tag.

**See Also:** TAG_COMPRESSION

,

Constant Field Values

- COMPRESSION_CCITT_RLE

```java
public static final int COMPRESSION_CCITT_RLE
```

A value to be used with the "Compression" tag.

**See Also:** TAG_COMPRESSION

,

Constant Field Values

- COMPRESSION_CCITT_T_4

```java
public static final int COMPRESSION_CCITT_T_4
```

A value to be used with the "Compression" tag.

**See Also:** TAG_COMPRESSION

,

Constant Field Values

- COMPRESSION_CCITT_T_6

```java
public static final int COMPRESSION_CCITT_T_6
```

A value to be used with the "Compression" tag.

**See Also:** TAG_COMPRESSION

,

Constant Field Values

- COMPRESSION_LZW

```java
public static final int COMPRESSION_LZW
```

A value to be used with the "Compression" tag.

**See Also:** TAG_COMPRESSION

,

Constant Field Values

- COMPRESSION_OLD_JPEG

```java
public static final int COMPRESSION_OLD_JPEG
```

A value to be used with the "Compression" tag.

**See Also:** TAG_COMPRESSION

,

Constant Field Values

- COMPRESSION_JPEG

```java
public static final int COMPRESSION_JPEG
```

A value to be used with the "Compression" tag.

**See Also:** TAG_COMPRESSION

,

Constant Field Values

- COMPRESSION_ZLIB

```java
public static final int COMPRESSION_ZLIB
```

A value to be used with the "Compression" tag.

**See Also:** TAG_COMPRESSION

,

Constant Field Values

- COMPRESSION_PACKBITS

```java
public static final int COMPRESSION_PACKBITS
```

A value to be used with the "Compression" tag.

**See Also:** TAG_COMPRESSION

,

Constant Field Values

- COMPRESSION_DEFLATE

```java
public static final int COMPRESSION_DEFLATE
```

A value to be used with the "Compression" tag.

**See Also:** TAG_COMPRESSION

,

DEFLATE specification

,

Constant Field Values

- TAG_PHOTOMETRIC_INTERPRETATION

```java
public static final int TAG_PHOTOMETRIC_INTERPRETATION
```

Constant specifying the "PhotometricInterpretation" tag.

**See Also:** PHOTOMETRIC_INTERPRETATION_WHITE_IS_ZERO

,

PHOTOMETRIC_INTERPRETATION_BLACK_IS_ZERO

,

PHOTOMETRIC_INTERPRETATION_RGB

,

PHOTOMETRIC_INTERPRETATION_PALETTE_COLOR

,

PHOTOMETRIC_INTERPRETATION_TRANSPARENCY_MASK

,

PHOTOMETRIC_INTERPRETATION_Y_CB_CR

,

PHOTOMETRIC_INTERPRETATION_CIELAB

,

PHOTOMETRIC_INTERPRETATION_ICCLAB

,

Constant Field Values

- PHOTOMETRIC_INTERPRETATION_WHITE_IS_ZERO

```java
public static final int PHOTOMETRIC_INTERPRETATION_WHITE_IS_ZERO
```

A value to be used with the "PhotometricInterpretation" tag.

**See Also:** TAG_PHOTOMETRIC_INTERPRETATION

,

Constant Field Values

- PHOTOMETRIC_INTERPRETATION_BLACK_IS_ZERO

```java
public static final int PHOTOMETRIC_INTERPRETATION_BLACK_IS_ZERO
```

A value to be used with the "PhotometricInterpretation" tag.

**See Also:** TAG_PHOTOMETRIC_INTERPRETATION

,

Constant Field Values

- PHOTOMETRIC_INTERPRETATION_RGB

```java
public static final int PHOTOMETRIC_INTERPRETATION_RGB
```

A value to be used with the "PhotometricInterpretation" tag.

**See Also:** TAG_PHOTOMETRIC_INTERPRETATION

,

Constant Field Values

- PHOTOMETRIC_INTERPRETATION_PALETTE_COLOR

```java
public static final int PHOTOMETRIC_INTERPRETATION_PALETTE_COLOR
```

A value to be used with the "PhotometricInterpretation" tag.

**See Also:** TAG_PHOTOMETRIC_INTERPRETATION

,

Constant Field Values

- PHOTOMETRIC_INTERPRETATION_TRANSPARENCY_MASK

```java
public static final int PHOTOMETRIC_INTERPRETATION_TRANSPARENCY_MASK
```

A value to be used with the "PhotometricInterpretation" tag.

**See Also:** TAG_PHOTOMETRIC_INTERPRETATION

,

Constant Field Values

- PHOTOMETRIC_INTERPRETATION_CMYK

```java
public static final int PHOTOMETRIC_INTERPRETATION_CMYK
```

A value to be used with the "PhotometricInterpretation" tag.

**See Also:** TAG_PHOTOMETRIC_INTERPRETATION

,

Constant Field Values

- PHOTOMETRIC_INTERPRETATION_Y_CB_CR

```java
public static final int PHOTOMETRIC_INTERPRETATION_Y_CB_CR
```

A value to be used with the "PhotometricInterpretation" tag.

**See Also:** TAG_PHOTOMETRIC_INTERPRETATION

,

Constant Field Values

- PHOTOMETRIC_INTERPRETATION_CIELAB

```java
public static final int PHOTOMETRIC_INTERPRETATION_CIELAB
```

A value to be used with the "PhotometricInterpretation" tag.

**See Also:** TAG_PHOTOMETRIC_INTERPRETATION

,

Constant Field Values

- PHOTOMETRIC_INTERPRETATION_ICCLAB

```java
public static final int PHOTOMETRIC_INTERPRETATION_ICCLAB
```

A value to be used with the "PhotometricInterpretation" tag.

**See Also:** TAG_PHOTOMETRIC_INTERPRETATION

,

Constant Field Values

- TAG_THRESHHOLDING

```java
public static final int TAG_THRESHHOLDING
```

Constant specifying the "Threshholding" tag.

**See Also:** THRESHHOLDING_NONE

,

THRESHHOLDING_ORDERED_DITHER

,

THRESHHOLDING_RANDOMIZED_DITHER

,

Constant Field Values

- THRESHHOLDING_NONE

```java
public static final int THRESHHOLDING_NONE
```

A value to be used with the "Thresholding" tag.

**See Also:** TAG_THRESHHOLDING

,

Constant Field Values

- THRESHHOLDING_ORDERED_DITHER

```java
public static final int THRESHHOLDING_ORDERED_DITHER
```

A value to be used with the "Thresholding" tag.

**See Also:** TAG_THRESHHOLDING

,

Constant Field Values

- THRESHHOLDING_RANDOMIZED_DITHER

```java
public static final int THRESHHOLDING_RANDOMIZED_DITHER
```

A value to be used with the "Thresholding" tag.

**See Also:** TAG_THRESHHOLDING

,

Constant Field Values

- TAG_CELL_WIDTH

```java
public static final int TAG_CELL_WIDTH
```

Constant specifying the "Cell_Width" tag.

**See Also:** Constant Field Values

- TAG_CELL_LENGTH

```java
public static final int TAG_CELL_LENGTH
```

Constant specifying the "cell_length" tag.

**See Also:** Constant Field Values

- TAG_FILL_ORDER

```java
public static final int TAG_FILL_ORDER
```

Constant specifying the "fill_order" tag.

**See Also:** FILL_ORDER_LEFT_TO_RIGHT

,

FILL_ORDER_RIGHT_TO_LEFT

,

Constant Field Values

- FILL_ORDER_LEFT_TO_RIGHT

```java
public static final int FILL_ORDER_LEFT_TO_RIGHT
```

A value to be used with the "FillOrder" tag.

**See Also:** TAG_FILL_ORDER

,

Constant Field Values

- FILL_ORDER_RIGHT_TO_LEFT

```java
public static final int FILL_ORDER_RIGHT_TO_LEFT
```

A value to be used with the "FillOrder" tag.

**See Also:** TAG_FILL_ORDER

,

Constant Field Values

- TAG_DOCUMENT_NAME

```java
public static final int TAG_DOCUMENT_NAME
```

Constant specifying the "document_name" tag.

**See Also:** Constant Field Values

- TAG_IMAGE_DESCRIPTION

```java
public static final int TAG_IMAGE_DESCRIPTION
```

Constant specifying the "Image_description" tag.

**See Also:** Constant Field Values

- TAG_MAKE

```java
public static final int TAG_MAKE
```

Constant specifying the "Make" tag.

**See Also:** Constant Field Values

- TAG_MODEL

```java
public static final int TAG_MODEL
```

Constant specifying the "Model" tag.

**See Also:** Constant Field Values

- TAG_STRIP_OFFSETS

```java
public static final int TAG_STRIP_OFFSETS
```

Constant specifying the "Strip_offsets" tag.

**See Also:** Constant Field Values

- TAG_ORIENTATION

```java
public static final int TAG_ORIENTATION
```

Constant specifying the "Orientation" tag.

**See Also:** ORIENTATION_ROW_0_TOP_COLUMN_0_LEFT

,

ORIENTATION_ROW_0_TOP_COLUMN_0_RIGHT

,

ORIENTATION_ROW_0_BOTTOM_COLUMN_0_RIGHT

,

ORIENTATION_ROW_0_BOTTOM_COLUMN_0_LEFT

,

ORIENTATION_ROW_0_LEFT_COLUMN_0_TOP

,

ORIENTATION_ROW_0_RIGHT_COLUMN_0_TOP

,

ORIENTATION_ROW_0_RIGHT_COLUMN_0_BOTTOM

,

ORIENTATION_ROW_0_LEFT_COLUMN_0_BOTTOM

,

Constant Field Values

- ORIENTATION_ROW_0_TOP_COLUMN_0_LEFT

```java
public static final int ORIENTATION_ROW_0_TOP_COLUMN_0_LEFT
```

A value to be used with the "Orientation" tag.

**See Also:** TAG_ORIENTATION

,

Constant Field Values

- ORIENTATION_ROW_0_TOP_COLUMN_0_RIGHT

```java
public static final int ORIENTATION_ROW_0_TOP_COLUMN_0_RIGHT
```

A value to be used with the "Orientation" tag.

**See Also:** TAG_ORIENTATION

,

Constant Field Values

- ORIENTATION_ROW_0_BOTTOM_COLUMN_0_RIGHT

```java
public static final int ORIENTATION_ROW_0_BOTTOM_COLUMN_0_RIGHT
```

A value to be used with the "Orientation" tag.

**See Also:** TAG_ORIENTATION

,

Constant Field Values

- ORIENTATION_ROW_0_BOTTOM_COLUMN_0_LEFT

```java
public static final int ORIENTATION_ROW_0_BOTTOM_COLUMN_0_LEFT
```

A value to be used with the "Orientation" tag.

**See Also:** TAG_ORIENTATION

,

Constant Field Values

- ORIENTATION_ROW_0_LEFT_COLUMN_0_TOP

```java
public static final int ORIENTATION_ROW_0_LEFT_COLUMN_0_TOP
```

A value to be used with the "Orientation" tag.

**See Also:** TAG_ORIENTATION

,

Constant Field Values

- ORIENTATION_ROW_0_RIGHT_COLUMN_0_TOP

```java
public static final int ORIENTATION_ROW_0_RIGHT_COLUMN_0_TOP
```

A value to be used with the "Orientation" tag.

**See Also:** TAG_ORIENTATION

,

Constant Field Values

- ORIENTATION_ROW_0_RIGHT_COLUMN_0_BOTTOM

```java
public static final int ORIENTATION_ROW_0_RIGHT_COLUMN_0_BOTTOM
```

A value to be used with the "Orientation" tag.

**See Also:** TAG_ORIENTATION

,

Constant Field Values

- ORIENTATION_ROW_0_LEFT_COLUMN_0_BOTTOM

```java
public static final int ORIENTATION_ROW_0_LEFT_COLUMN_0_BOTTOM
```

A value to be used with the "Orientation" tag.

**See Also:** TAG_ORIENTATION

,

Constant Field Values

- TAG_SAMPLES_PER_PIXEL

```java
public static final int TAG_SAMPLES_PER_PIXEL
```

Constant specifying the "Samples_per_pixel" tag.

**See Also:** Constant Field Values

- TAG_ROWS_PER_STRIP

```java
public static final int TAG_ROWS_PER_STRIP
```

Constant specifying the "Rows_per_strip" tag.

**See Also:** Constant Field Values

- TAG_STRIP_BYTE_COUNTS

```java
public static final int TAG_STRIP_BYTE_COUNTS
```

Constant specifying the "Strip_byte_counts" tag.

**See Also:** Constant Field Values

- TAG_MIN_SAMPLE_VALUE

```java
public static final int TAG_MIN_SAMPLE_VALUE
```

Constant specifying the "Min_sample_value" tag.

**See Also:** Constant Field Values

- TAG_MAX_SAMPLE_VALUE

```java
public static final int TAG_MAX_SAMPLE_VALUE
```

Constant specifying the "Max_sample_value" tag.

**See Also:** Constant Field Values

- TAG_X_RESOLUTION

```java
public static final int TAG_X_RESOLUTION
```

Constant specifying the "XResolution" tag.

**See Also:** Constant Field Values

- TAG_Y_RESOLUTION

```java
public static final int TAG_Y_RESOLUTION
```

Constant specifying the "YResolution" tag.

**See Also:** Constant Field Values

- TAG_PLANAR_CONFIGURATION

```java
public static final int TAG_PLANAR_CONFIGURATION
```

Constant specifying the "PlanarConfiguration" tag.

**See Also:** PLANAR_CONFIGURATION_CHUNKY

,

PLANAR_CONFIGURATION_PLANAR

,

Constant Field Values

- PLANAR_CONFIGURATION_CHUNKY

```java
public static final int PLANAR_CONFIGURATION_CHUNKY
```

A value to be used with the "PlanarConfiguration" tag.

**See Also:** TAG_PLANAR_CONFIGURATION

,

Constant Field Values

- PLANAR_CONFIGURATION_PLANAR

```java
public static final int PLANAR_CONFIGURATION_PLANAR
```

A value to be used with the "PlanarConfiguration" tag.

**See Also:** TAG_PLANAR_CONFIGURATION

,

Constant Field Values

- TAG_PAGE_NAME

```java
public static final int TAG_PAGE_NAME
```

Constant specifying the "PageName" tag.

**See Also:** Constant Field Values

- TAG_X_POSITION

```java
public static final int TAG_X_POSITION
```

Constant specifying the "XPosition" tag.

**See Also:** Constant Field Values

- TAG_Y_POSITION

```java
public static final int TAG_Y_POSITION
```

Constant specifying the "YPosition" tag.

**See Also:** Constant Field Values

- TAG_FREE_OFFSETS

```java
public static final int TAG_FREE_OFFSETS
```

Constant specifying the "FreeOffsets" tag.

**See Also:** Constant Field Values

- TAG_FREE_BYTE_COUNTS

```java
public static final int TAG_FREE_BYTE_COUNTS
```

Constant specifying the "FreeByteCounts" tag.

**See Also:** Constant Field Values

- TAG_GRAY_RESPONSE_UNIT

```java
public static final int TAG_GRAY_RESPONSE_UNIT
```

Constant specifying the "GrayResponseUnit" tag.

**See Also:** GRAY_RESPONSE_UNIT_TENTHS

,

GRAY_RESPONSE_UNIT_HUNDREDTHS

,

GRAY_RESPONSE_UNIT_THOUSANDTHS

,

GRAY_RESPONSE_UNIT_TEN_THOUSANDTHS

,

GRAY_RESPONSE_UNIT_HUNDRED_THOUSANDTHS

,

Constant Field Values

- GRAY_RESPONSE_UNIT_TENTHS

```java
public static final int GRAY_RESPONSE_UNIT_TENTHS
```

A value to be used with the "GrayResponseUnit" tag.

**See Also:** TAG_GRAY_RESPONSE_UNIT

,

Constant Field Values

- GRAY_RESPONSE_UNIT_HUNDREDTHS

```java
public static final int GRAY_RESPONSE_UNIT_HUNDREDTHS
```

A value to be used with the "GrayResponseUnit" tag.

**See Also:** TAG_GRAY_RESPONSE_UNIT

,

Constant Field Values

- GRAY_RESPONSE_UNIT_THOUSANDTHS

```java
public static final int GRAY_RESPONSE_UNIT_THOUSANDTHS
```

A value to be used with the "GrayResponseUnit" tag.

**See Also:** TAG_GRAY_RESPONSE_UNIT

,

Constant Field Values

- GRAY_RESPONSE_UNIT_TEN_THOUSANDTHS

```java
public static final int GRAY_RESPONSE_UNIT_TEN_THOUSANDTHS
```

A value to be used with the "GrayResponseUnit" tag.

**See Also:** TAG_GRAY_RESPONSE_UNIT

,

Constant Field Values

- GRAY_RESPONSE_UNIT_HUNDRED_THOUSANDTHS

```java
public static final int GRAY_RESPONSE_UNIT_HUNDRED_THOUSANDTHS
```

A value to be used with the "GrayResponseUnit" tag.

**See Also:** TAG_GRAY_RESPONSE_UNIT

,

Constant Field Values

- TAG_GRAY_RESPONSE_CURVE

```java
public static final int TAG_GRAY_RESPONSE_CURVE
```

Constant specifying the "GrayResponseCurve" tag.

**See Also:** Constant Field Values

- TAG_T4_OPTIONS

```java
public static final int TAG_T4_OPTIONS
```

Constant specifying the "T4Options" tag.

**See Also:** T4_OPTIONS_2D_CODING

,

T4_OPTIONS_UNCOMPRESSED

,

T4_OPTIONS_EOL_BYTE_ALIGNED

,

Constant Field Values

- T4_OPTIONS_2D_CODING

```java
public static final int T4_OPTIONS_2D_CODING
```

A mask to be used with the "T4Options" tag.

**See Also:** TAG_T4_OPTIONS

,

Constant Field Values

- T4_OPTIONS_UNCOMPRESSED

```java
public static final int T4_OPTIONS_UNCOMPRESSED
```

A mask to be used with the "T4Options" tag.

**See Also:** TAG_T4_OPTIONS

,

Constant Field Values

- T4_OPTIONS_EOL_BYTE_ALIGNED

```java
public static final int T4_OPTIONS_EOL_BYTE_ALIGNED
```

A mask to be used with the "T4Options" tag.

**See Also:** TAG_T4_OPTIONS

,

Constant Field Values

- TAG_T6_OPTIONS

```java
public static final int TAG_T6_OPTIONS
```

Constant specifying the "T6Options" tag.

**See Also:** T6_OPTIONS_UNCOMPRESSED

,

Constant Field Values

- T6_OPTIONS_UNCOMPRESSED

```java
public static final int T6_OPTIONS_UNCOMPRESSED
```

A mask to be used with the "T6Options" tag.

**See Also:** TAG_T6_OPTIONS

,

Constant Field Values

- TAG_RESOLUTION_UNIT

```java
public static final int TAG_RESOLUTION_UNIT
```

Constant specifying the "ResolutionUnit" tag.

**See Also:** RESOLUTION_UNIT_NONE

,

RESOLUTION_UNIT_INCH

,

RESOLUTION_UNIT_CENTIMETER

,

Constant Field Values

- RESOLUTION_UNIT_NONE

```java
public static final int RESOLUTION_UNIT_NONE
```

A value to be used with the "ResolutionUnit" tag.

**See Also:** TAG_RESOLUTION_UNIT

,

Constant Field Values

- RESOLUTION_UNIT_INCH

```java
public static final int RESOLUTION_UNIT_INCH
```

A value to be used with the "ResolutionUnit" tag.

**See Also:** TAG_RESOLUTION_UNIT

,

Constant Field Values

- RESOLUTION_UNIT_CENTIMETER

```java
public static final int RESOLUTION_UNIT_CENTIMETER
```

A value to be used with the "ResolutionUnit" tag.

**See Also:** TAG_RESOLUTION_UNIT

,

Constant Field Values

- TAG_PAGE_NUMBER

```java
public static final int TAG_PAGE_NUMBER
```

Constant specifying the "PageNumber" tag.

**See Also:** Constant Field Values

- TAG_TRANSFER_FUNCTION

```java
public static final int TAG_TRANSFER_FUNCTION
```

Constant specifying the "TransferFunction" tag.

**See Also:** Constant Field Values

- TAG_SOFTWARE

```java
public static final int TAG_SOFTWARE
```

Constant specifying the "Software" tag.

**See Also:** Constant Field Values

- TAG_DATE_TIME

```java
public static final int TAG_DATE_TIME
```

Constant specifying the "DateTime" tag.

**See Also:** Constant Field Values

- TAG_ARTIST

```java
public static final int TAG_ARTIST
```

Constant specifying the "Artist" tag.

**See Also:** Constant Field Values

- TAG_HOST_COMPUTER

```java
public static final int TAG_HOST_COMPUTER
```

Constant specifying the "HostComputer" tag.

**See Also:** Constant Field Values

- TAG_PREDICTOR

```java
public static final int TAG_PREDICTOR
```

Constant specifying the "Predictor" tag.

**See Also:** TAG_WHITE_POINT

,

TAG_PRIMARY_CHROMATICITES

,

TAG_COLOR_MAP

,

TAG_HALFTONE_HINTS

,

TAG_TILE_WIDTH

,

TAG_TILE_LENGTH

,

TAG_TILE_OFFSETS

,

TAG_TILE_BYTE_COUNTS

,

Constant Field Values

- PREDICTOR_NONE

```java
public static final int PREDICTOR_NONE
```

A value to be used with the "Predictor" tag.

**See Also:** TAG_PREDICTOR

,

Constant Field Values

- PREDICTOR_HORIZONTAL_DIFFERENCING

```java
public static final int PREDICTOR_HORIZONTAL_DIFFERENCING
```

A value to be used with the "Predictor" tag.

**See Also:** TAG_PREDICTOR

,

Constant Field Values

- TAG_WHITE_POINT

```java
public static final int TAG_WHITE_POINT
```

Constant specifying the "WhitePoint" tag.

**See Also:** Constant Field Values

- TAG_PRIMARY_CHROMATICITES

```java
public static final int TAG_PRIMARY_CHROMATICITES
```

Constant specifying the "PrimaryChromaticites" tag.

**See Also:** Constant Field Values

- TAG_COLOR_MAP

```java
public static final int TAG_COLOR_MAP
```

Constant specifying the "ColorMap" tag.

**See Also:** Constant Field Values

- TAG_HALFTONE_HINTS

```java
public static final int TAG_HALFTONE_HINTS
```

Constant specifying the "HalftoneHints" tag.

**See Also:** Constant Field Values

- TAG_TILE_WIDTH

```java
public static final int TAG_TILE_WIDTH
```

Constant specifying the "TileWidth" tag.

**See Also:** Constant Field Values

- TAG_TILE_LENGTH

```java
public static final int TAG_TILE_LENGTH
```

Constant specifying the "TileLength" tag.

**See Also:** Constant Field Values

- TAG_TILE_OFFSETS

```java
public static final int TAG_TILE_OFFSETS
```

Constant specifying the "TileOffsets" tag.

**See Also:** Constant Field Values

- TAG_TILE_BYTE_COUNTS

```java
public static final int TAG_TILE_BYTE_COUNTS
```

Constant specifying the "TileByteCounts" tag.

**See Also:** Constant Field Values

- TAG_INK_SET

```java
public static final int TAG_INK_SET
```

Constant specifying the "InkSet" tag.

**See Also:** INK_SET_CMYK

,

INK_SET_NOT_CMYK

,

Constant Field Values

- INK_SET_CMYK

```java
public static final int INK_SET_CMYK
```

A value to be used with the "InkSet" tag.

**See Also:** TAG_INK_SET

,

Constant Field Values

- INK_SET_NOT_CMYK

```java
public static final int INK_SET_NOT_CMYK
```

A value to be used with the "InkSet" tag.

**See Also:** TAG_INK_SET

,

Constant Field Values

- TAG_INK_NAMES

```java
public static final int TAG_INK_NAMES
```

Constant specifying the "InkNames" tag.

**See Also:** Constant Field Values

- TAG_NUMBER_OF_INKS

```java
public static final int TAG_NUMBER_OF_INKS
```

Constant specifying the "NumberOfInks" tag.

**See Also:** Constant Field Values

- TAG_DOT_RANGE

```java
public static final int TAG_DOT_RANGE
```

Constant specifying the "DotRange" tag.

**See Also:** Constant Field Values

- TAG_TARGET_PRINTER

```java
public static final int TAG_TARGET_PRINTER
```

Constant specifying the "TargetPrinter" tag.

**See Also:** Constant Field Values

- TAG_EXTRA_SAMPLES

```java
public static final int TAG_EXTRA_SAMPLES
```

Constant specifying the "ExtraSamples" tag.

**See Also:** EXTRA_SAMPLES_UNSPECIFIED

,

EXTRA_SAMPLES_ASSOCIATED_ALPHA

,

EXTRA_SAMPLES_UNASSOCIATED_ALPHA

,

Constant Field Values

- EXTRA_SAMPLES_UNSPECIFIED

```java
public static final int EXTRA_SAMPLES_UNSPECIFIED
```

A value to be used with the "ExtraSamples" tag.

**See Also:** TAG_EXTRA_SAMPLES

,

Constant Field Values

- EXTRA_SAMPLES_ASSOCIATED_ALPHA

```java
public static final int EXTRA_SAMPLES_ASSOCIATED_ALPHA
```

A value to be used with the "ExtraSamples" tag.

**See Also:** TAG_EXTRA_SAMPLES

,

Constant Field Values

- EXTRA_SAMPLES_UNASSOCIATED_ALPHA

```java
public static final int EXTRA_SAMPLES_UNASSOCIATED_ALPHA
```

A value to be used with the "ExtraSamples" tag.

**See Also:** TAG_EXTRA_SAMPLES

,

Constant Field Values

- TAG_SAMPLE_FORMAT

```java
public static final int TAG_SAMPLE_FORMAT
```

Constant specifying the "SampleFormat" tag.

**See Also:** SAMPLE_FORMAT_UNSIGNED_INTEGER

,

SAMPLE_FORMAT_SIGNED_INTEGER

,

SAMPLE_FORMAT_FLOATING_POINT

,

SAMPLE_FORMAT_UNDEFINED

,

Constant Field Values

- SAMPLE_FORMAT_UNSIGNED_INTEGER

```java
public static final int SAMPLE_FORMAT_UNSIGNED_INTEGER
```

A value to be used with the "SampleFormat" tag.

**See Also:** TAG_SAMPLE_FORMAT

,

Constant Field Values

- SAMPLE_FORMAT_SIGNED_INTEGER

```java
public static final int SAMPLE_FORMAT_SIGNED_INTEGER
```

A value to be used with the "SampleFormat" tag.

**See Also:** TAG_SAMPLE_FORMAT

,

Constant Field Values

- SAMPLE_FORMAT_FLOATING_POINT

```java
public static final int SAMPLE_FORMAT_FLOATING_POINT
```

A value to be used with the "SampleFormat" tag.

**See Also:** TAG_SAMPLE_FORMAT

,

Constant Field Values

- SAMPLE_FORMAT_UNDEFINED

```java
public static final int SAMPLE_FORMAT_UNDEFINED
```

A value to be used with the "SampleFormat" tag.

**See Also:** TAG_SAMPLE_FORMAT

,

Constant Field Values

- TAG_S_MIN_SAMPLE_VALUE

```java
public static final int TAG_S_MIN_SAMPLE_VALUE
```

Constant specifying the "SMinSampleValue" tag.

**See Also:** Constant Field Values

- TAG_S_MAX_SAMPLE_VALUE

```java
public static final int TAG_S_MAX_SAMPLE_VALUE
```

Constant specifying the "SMaxSampleValue" tag.

**See Also:** Constant Field Values

- TAG_TRANSFER_RANGE

```java
public static final int TAG_TRANSFER_RANGE
```

Constant specifying the "TransferRange" tag.

**See Also:** Constant Field Values

- TAG_JPEG_TABLES

```java
public static final int TAG_JPEG_TABLES
```

Constant specifying the "JPEGTables" tag.

**See Also:** JPEG-in-TIFF compression

,

Constant Field Values

- TAG_JPEG_PROC

```java
public static final int TAG_JPEG_PROC
```

Constant specifying the "JPEGProc" tag.

**See Also:** Constant Field Values

- JPEG_PROC_BASELINE

```java
public static final int JPEG_PROC_BASELINE
```

A value to be used with the "JPEGProc" tag.

**See Also:** TAG_JPEG_PROC

,

Constant Field Values

- JPEG_PROC_LOSSLESS

```java
public static final int JPEG_PROC_LOSSLESS
```

A value to be used with the "JPEGProc" tag.

**See Also:** TAG_JPEG_PROC

,

Constant Field Values

- TAG_JPEG_INTERCHANGE_FORMAT

```java
public static final int TAG_JPEG_INTERCHANGE_FORMAT
```

Constant specifying the "JPEGInterchangeFormat" tag.

**See Also:** Constant Field Values

- TAG_JPEG_INTERCHANGE_FORMAT_LENGTH

```java
public static final int TAG_JPEG_INTERCHANGE_FORMAT_LENGTH
```

Constant specifying the "JPEGInterchangeFormatLength" tag.

**See Also:** Constant Field Values

- TAG_JPEG_RESTART_INTERVAL

```java
public static final int TAG_JPEG_RESTART_INTERVAL
```

Constant specifying the "JPEGRestartInterval" tag.

**See Also:** Constant Field Values

- TAG_JPEG_LOSSLESS_PREDICTORS

```java
public static final int TAG_JPEG_LOSSLESS_PREDICTORS
```

Constant specifying the "JPEGLosslessPredictors" tag.

**See Also:** Constant Field Values

- TAG_JPEG_POINT_TRANSFORMS

```java
public static final int TAG_JPEG_POINT_TRANSFORMS
```

Constant specifying the "JPEGPointTransforms" tag.

**See Also:** Constant Field Values

- TAG_JPEG_Q_TABLES

```java
public static final int TAG_JPEG_Q_TABLES
```

Constant specifying the "JPEGQTables" tag.

**See Also:** Constant Field Values

- TAG_JPEG_DC_TABLES

```java
public static final int TAG_JPEG_DC_TABLES
```

Constant specifying the "JPEGDCTables" tag.

**See Also:** Constant Field Values

- TAG_JPEG_AC_TABLES

```java
public static final int TAG_JPEG_AC_TABLES
```

Constant specifying the "JPEGACTables" tag.

**See Also:** Constant Field Values

- TAG_Y_CB_CR_COEFFICIENTS

```java
public static final int TAG_Y_CB_CR_COEFFICIENTS
```

Constant specifying the "YCbCrCoefficients" tag.

**See Also:** Constant Field Values

- TAG_Y_CB_CR_SUBSAMPLING

```java
public static final int TAG_Y_CB_CR_SUBSAMPLING
```

Constant specifying the "YCbCrSubsampling" tag.

**See Also:** Constant Field Values

- TAG_Y_CB_CR_POSITIONING

```java
public static final int TAG_Y_CB_CR_POSITIONING
```

Constant specifying the "YCbCrPositioning" tag.

**See Also:** Y_CB_CR_POSITIONING_CENTERED

,

Y_CB_CR_POSITIONING_COSITED

,

Constant Field Values

- Y_CB_CR_POSITIONING_CENTERED

```java
public static final int Y_CB_CR_POSITIONING_CENTERED
```

A value to be used with the "YCbCrPositioning" tag.

**See Also:** TAG_Y_CB_CR_POSITIONING

,

Constant Field Values

- Y_CB_CR_POSITIONING_COSITED

```java
public static final int Y_CB_CR_POSITIONING_COSITED
```

A value to be used with the "YCbCrPositioning" tag.

**See Also:** TAG_Y_CB_CR_POSITIONING

,

Constant Field Values

- TAG_REFERENCE_BLACK_WHITE

```java
public static final int TAG_REFERENCE_BLACK_WHITE
```

Constant specifying the "ReferenceBlackWhite" tag.

**See Also:** Constant Field Values

- TAG_COPYRIGHT

```java
public static final int TAG_COPYRIGHT
```

Constant specifying the "Copyright" tag.

**See Also:** Constant Field Values

- TAG_ICC_PROFILE

```java
public static final int TAG_ICC_PROFILE
```

Constant specifying the "ICC Profile" tag.

**See Also:** ICC Specification, section B.4: Embedding ICC profiles in TIFF files

,

Constant Field Values

---

#### Field Detail

TAG_NEW_SUBFILE_TYPE

```java
public static final int TAG_NEW_SUBFILE_TYPE
```

Constant specifying the "NewSubfileType" tag.

**See Also:** NEW_SUBFILE_TYPE_REDUCED_RESOLUTION

,

NEW_SUBFILE_TYPE_SINGLE_PAGE

,

NEW_SUBFILE_TYPE_TRANSPARENCY

,

Constant Field Values

---

#### TAG_NEW_SUBFILE_TYPE

public static final int TAG_NEW_SUBFILE_TYPE

Constant specifying the "NewSubfileType" tag.

NEW_SUBFILE_TYPE_REDUCED_RESOLUTION

```java
public static final int NEW_SUBFILE_TYPE_REDUCED_RESOLUTION
```

A mask to be used with the "NewSubfileType" tag.

**See Also:** TAG_NEW_SUBFILE_TYPE

,

Constant Field Values

---

#### NEW_SUBFILE_TYPE_REDUCED_RESOLUTION

public static final int NEW_SUBFILE_TYPE_REDUCED_RESOLUTION

A mask to be used with the "NewSubfileType" tag.

NEW_SUBFILE_TYPE_SINGLE_PAGE

```java
public static final int NEW_SUBFILE_TYPE_SINGLE_PAGE
```

A mask to be used with the "NewSubfileType" tag.

**See Also:** TAG_NEW_SUBFILE_TYPE

,

Constant Field Values

---

#### NEW_SUBFILE_TYPE_SINGLE_PAGE

public static final int NEW_SUBFILE_TYPE_SINGLE_PAGE

A mask to be used with the "NewSubfileType" tag.

NEW_SUBFILE_TYPE_TRANSPARENCY

```java
public static final int NEW_SUBFILE_TYPE_TRANSPARENCY
```

A mask to be used with the "NewSubfileType" tag.

**See Also:** TAG_NEW_SUBFILE_TYPE

,

Constant Field Values

---

#### NEW_SUBFILE_TYPE_TRANSPARENCY

public static final int NEW_SUBFILE_TYPE_TRANSPARENCY

A mask to be used with the "NewSubfileType" tag.

TAG_SUBFILE_TYPE

```java
public static final int TAG_SUBFILE_TYPE
```

Constant specifying the "SubfileType" tag.

**See Also:** SUBFILE_TYPE_FULL_RESOLUTION

,

SUBFILE_TYPE_REDUCED_RESOLUTION

,

SUBFILE_TYPE_SINGLE_PAGE

,

Constant Field Values

---

#### TAG_SUBFILE_TYPE

public static final int TAG_SUBFILE_TYPE

Constant specifying the "SubfileType" tag.

SUBFILE_TYPE_FULL_RESOLUTION

```java
public static final int SUBFILE_TYPE_FULL_RESOLUTION
```

A value to be used with the "SubfileType" tag.

**See Also:** TAG_SUBFILE_TYPE

,

Constant Field Values

---

#### SUBFILE_TYPE_FULL_RESOLUTION

public static final int SUBFILE_TYPE_FULL_RESOLUTION

A value to be used with the "SubfileType" tag.

SUBFILE_TYPE_REDUCED_RESOLUTION

```java
public static final int SUBFILE_TYPE_REDUCED_RESOLUTION
```

A value to be used with the "SubfileType" tag.

**See Also:** TAG_SUBFILE_TYPE

,

Constant Field Values

---

#### SUBFILE_TYPE_REDUCED_RESOLUTION

public static final int SUBFILE_TYPE_REDUCED_RESOLUTION

A value to be used with the "SubfileType" tag.

SUBFILE_TYPE_SINGLE_PAGE

```java
public static final int SUBFILE_TYPE_SINGLE_PAGE
```

A value to be used with the "SubfileType" tag.

**See Also:** TAG_SUBFILE_TYPE

,

Constant Field Values

---

#### SUBFILE_TYPE_SINGLE_PAGE

public static final int SUBFILE_TYPE_SINGLE_PAGE

A value to be used with the "SubfileType" tag.

TAG_IMAGE_WIDTH

```java
public static final int TAG_IMAGE_WIDTH
```

Constant specifying the "ImageWidth" tag.

**See Also:** Constant Field Values

---

#### TAG_IMAGE_WIDTH

public static final int TAG_IMAGE_WIDTH

Constant specifying the "ImageWidth" tag.

TAG_IMAGE_LENGTH

```java
public static final int TAG_IMAGE_LENGTH
```

Constant specifying the "ImageLength" tag.

**See Also:** Constant Field Values

---

#### TAG_IMAGE_LENGTH

public static final int TAG_IMAGE_LENGTH

Constant specifying the "ImageLength" tag.

TAG_BITS_PER_SAMPLE

```java
public static final int TAG_BITS_PER_SAMPLE
```

Constant specifying the "BitsPerSample" tag.

**See Also:** Constant Field Values

---

#### TAG_BITS_PER_SAMPLE

public static final int TAG_BITS_PER_SAMPLE

Constant specifying the "BitsPerSample" tag.

TAG_COMPRESSION

```java
public static final int TAG_COMPRESSION
```

Constant specifying the "Compression" tag.

**See Also:** COMPRESSION_NONE

,

COMPRESSION_CCITT_RLE

,

COMPRESSION_CCITT_T_4

,

COMPRESSION_CCITT_T_6

,

COMPRESSION_LZW

,

COMPRESSION_OLD_JPEG

,

COMPRESSION_JPEG

,

COMPRESSION_ZLIB

,

COMPRESSION_PACKBITS

,

COMPRESSION_DEFLATE

,

Constant Field Values

---

#### TAG_COMPRESSION

public static final int TAG_COMPRESSION

Constant specifying the "Compression" tag.

COMPRESSION_NONE

```java
public static final int COMPRESSION_NONE
```

A value to be used with the "Compression" tag.

**See Also:** TAG_COMPRESSION

,

Constant Field Values

---

#### COMPRESSION_NONE

public static final int COMPRESSION_NONE

A value to be used with the "Compression" tag.

COMPRESSION_CCITT_RLE

```java
public static final int COMPRESSION_CCITT_RLE
```

A value to be used with the "Compression" tag.

**See Also:** TAG_COMPRESSION

,

Constant Field Values

---

#### COMPRESSION_CCITT_RLE

public static final int COMPRESSION_CCITT_RLE

A value to be used with the "Compression" tag.

COMPRESSION_CCITT_T_4

```java
public static final int COMPRESSION_CCITT_T_4
```

A value to be used with the "Compression" tag.

**See Also:** TAG_COMPRESSION

,

Constant Field Values

---

#### COMPRESSION_CCITT_T_4

public static final int COMPRESSION_CCITT_T_4

A value to be used with the "Compression" tag.

COMPRESSION_CCITT_T_6

```java
public static final int COMPRESSION_CCITT_T_6
```

A value to be used with the "Compression" tag.

**See Also:** TAG_COMPRESSION

,

Constant Field Values

---

#### COMPRESSION_CCITT_T_6

public static final int COMPRESSION_CCITT_T_6

A value to be used with the "Compression" tag.

COMPRESSION_LZW

```java
public static final int COMPRESSION_LZW
```

A value to be used with the "Compression" tag.

**See Also:** TAG_COMPRESSION

,

Constant Field Values

---

#### COMPRESSION_LZW

public static final int COMPRESSION_LZW

A value to be used with the "Compression" tag.

COMPRESSION_OLD_JPEG

```java
public static final int COMPRESSION_OLD_JPEG
```

A value to be used with the "Compression" tag.

**See Also:** TAG_COMPRESSION

,

Constant Field Values

---

#### COMPRESSION_OLD_JPEG

public static final int COMPRESSION_OLD_JPEG

A value to be used with the "Compression" tag.

COMPRESSION_JPEG

```java
public static final int COMPRESSION_JPEG
```

A value to be used with the "Compression" tag.

**See Also:** TAG_COMPRESSION

,

Constant Field Values

---

#### COMPRESSION_JPEG

public static final int COMPRESSION_JPEG

A value to be used with the "Compression" tag.

COMPRESSION_ZLIB

```java
public static final int COMPRESSION_ZLIB
```

A value to be used with the "Compression" tag.

**See Also:** TAG_COMPRESSION

,

Constant Field Values

---

#### COMPRESSION_ZLIB

public static final int COMPRESSION_ZLIB

A value to be used with the "Compression" tag.

COMPRESSION_PACKBITS

```java
public static final int COMPRESSION_PACKBITS
```

A value to be used with the "Compression" tag.

**See Also:** TAG_COMPRESSION

,

Constant Field Values

---

#### COMPRESSION_PACKBITS

public static final int COMPRESSION_PACKBITS

A value to be used with the "Compression" tag.

COMPRESSION_DEFLATE

```java
public static final int COMPRESSION_DEFLATE
```

A value to be used with the "Compression" tag.

**See Also:** TAG_COMPRESSION

,

DEFLATE specification

,

Constant Field Values

---

#### COMPRESSION_DEFLATE

public static final int COMPRESSION_DEFLATE

A value to be used with the "Compression" tag.

TAG_PHOTOMETRIC_INTERPRETATION

```java
public static final int TAG_PHOTOMETRIC_INTERPRETATION
```

Constant specifying the "PhotometricInterpretation" tag.

**See Also:** PHOTOMETRIC_INTERPRETATION_WHITE_IS_ZERO

,

PHOTOMETRIC_INTERPRETATION_BLACK_IS_ZERO

,

PHOTOMETRIC_INTERPRETATION_RGB

,

PHOTOMETRIC_INTERPRETATION_PALETTE_COLOR

,

PHOTOMETRIC_INTERPRETATION_TRANSPARENCY_MASK

,

PHOTOMETRIC_INTERPRETATION_Y_CB_CR

,

PHOTOMETRIC_INTERPRETATION_CIELAB

,

PHOTOMETRIC_INTERPRETATION_ICCLAB

,

Constant Field Values

---

#### TAG_PHOTOMETRIC_INTERPRETATION

public static final int TAG_PHOTOMETRIC_INTERPRETATION

Constant specifying the "PhotometricInterpretation" tag.

PHOTOMETRIC_INTERPRETATION_WHITE_IS_ZERO

```java
public static final int PHOTOMETRIC_INTERPRETATION_WHITE_IS_ZERO
```

A value to be used with the "PhotometricInterpretation" tag.

**See Also:** TAG_PHOTOMETRIC_INTERPRETATION

,

Constant Field Values

---

#### PHOTOMETRIC_INTERPRETATION_WHITE_IS_ZERO

public static final int PHOTOMETRIC_INTERPRETATION_WHITE_IS_ZERO

A value to be used with the "PhotometricInterpretation" tag.

PHOTOMETRIC_INTERPRETATION_BLACK_IS_ZERO

```java
public static final int PHOTOMETRIC_INTERPRETATION_BLACK_IS_ZERO
```

A value to be used with the "PhotometricInterpretation" tag.

**See Also:** TAG_PHOTOMETRIC_INTERPRETATION

,

Constant Field Values

---

#### PHOTOMETRIC_INTERPRETATION_BLACK_IS_ZERO

public static final int PHOTOMETRIC_INTERPRETATION_BLACK_IS_ZERO

A value to be used with the "PhotometricInterpretation" tag.

PHOTOMETRIC_INTERPRETATION_RGB

```java
public static final int PHOTOMETRIC_INTERPRETATION_RGB
```

A value to be used with the "PhotometricInterpretation" tag.

**See Also:** TAG_PHOTOMETRIC_INTERPRETATION

,

Constant Field Values

---

#### PHOTOMETRIC_INTERPRETATION_RGB

public static final int PHOTOMETRIC_INTERPRETATION_RGB

A value to be used with the "PhotometricInterpretation" tag.

PHOTOMETRIC_INTERPRETATION_PALETTE_COLOR

```java
public static final int PHOTOMETRIC_INTERPRETATION_PALETTE_COLOR
```

A value to be used with the "PhotometricInterpretation" tag.

**See Also:** TAG_PHOTOMETRIC_INTERPRETATION

,

Constant Field Values

---

#### PHOTOMETRIC_INTERPRETATION_PALETTE_COLOR

public static final int PHOTOMETRIC_INTERPRETATION_PALETTE_COLOR

A value to be used with the "PhotometricInterpretation" tag.

PHOTOMETRIC_INTERPRETATION_TRANSPARENCY_MASK

```java
public static final int PHOTOMETRIC_INTERPRETATION_TRANSPARENCY_MASK
```

A value to be used with the "PhotometricInterpretation" tag.

**See Also:** TAG_PHOTOMETRIC_INTERPRETATION

,

Constant Field Values

---

#### PHOTOMETRIC_INTERPRETATION_TRANSPARENCY_MASK

public static final int PHOTOMETRIC_INTERPRETATION_TRANSPARENCY_MASK

A value to be used with the "PhotometricInterpretation" tag.

PHOTOMETRIC_INTERPRETATION_CMYK

```java
public static final int PHOTOMETRIC_INTERPRETATION_CMYK
```

A value to be used with the "PhotometricInterpretation" tag.

**See Also:** TAG_PHOTOMETRIC_INTERPRETATION

,

Constant Field Values

---

#### PHOTOMETRIC_INTERPRETATION_CMYK

public static final int PHOTOMETRIC_INTERPRETATION_CMYK

A value to be used with the "PhotometricInterpretation" tag.

PHOTOMETRIC_INTERPRETATION_Y_CB_CR

```java
public static final int PHOTOMETRIC_INTERPRETATION_Y_CB_CR
```

A value to be used with the "PhotometricInterpretation" tag.

**See Also:** TAG_PHOTOMETRIC_INTERPRETATION

,

Constant Field Values

---

#### PHOTOMETRIC_INTERPRETATION_Y_CB_CR

public static final int PHOTOMETRIC_INTERPRETATION_Y_CB_CR

A value to be used with the "PhotometricInterpretation" tag.

PHOTOMETRIC_INTERPRETATION_CIELAB

```java
public static final int PHOTOMETRIC_INTERPRETATION_CIELAB
```

A value to be used with the "PhotometricInterpretation" tag.

**See Also:** TAG_PHOTOMETRIC_INTERPRETATION

,

Constant Field Values

---

#### PHOTOMETRIC_INTERPRETATION_CIELAB

public static final int PHOTOMETRIC_INTERPRETATION_CIELAB

A value to be used with the "PhotometricInterpretation" tag.

PHOTOMETRIC_INTERPRETATION_ICCLAB

```java
public static final int PHOTOMETRIC_INTERPRETATION_ICCLAB
```

A value to be used with the "PhotometricInterpretation" tag.

**See Also:** TAG_PHOTOMETRIC_INTERPRETATION

,

Constant Field Values

---

#### PHOTOMETRIC_INTERPRETATION_ICCLAB

public static final int PHOTOMETRIC_INTERPRETATION_ICCLAB

A value to be used with the "PhotometricInterpretation" tag.

TAG_THRESHHOLDING

```java
public static final int TAG_THRESHHOLDING
```

Constant specifying the "Threshholding" tag.

**See Also:** THRESHHOLDING_NONE

,

THRESHHOLDING_ORDERED_DITHER

,

THRESHHOLDING_RANDOMIZED_DITHER

,

Constant Field Values

---

#### TAG_THRESHHOLDING

public static final int TAG_THRESHHOLDING

Constant specifying the "Threshholding" tag.

THRESHHOLDING_NONE

```java
public static final int THRESHHOLDING_NONE
```

A value to be used with the "Thresholding" tag.

**See Also:** TAG_THRESHHOLDING

,

Constant Field Values

---

#### THRESHHOLDING_NONE

public static final int THRESHHOLDING_NONE

A value to be used with the "Thresholding" tag.

THRESHHOLDING_ORDERED_DITHER

```java
public static final int THRESHHOLDING_ORDERED_DITHER
```

A value to be used with the "Thresholding" tag.

**See Also:** TAG_THRESHHOLDING

,

Constant Field Values

---

#### THRESHHOLDING_ORDERED_DITHER

public static final int THRESHHOLDING_ORDERED_DITHER

A value to be used with the "Thresholding" tag.

THRESHHOLDING_RANDOMIZED_DITHER

```java
public static final int THRESHHOLDING_RANDOMIZED_DITHER
```

A value to be used with the "Thresholding" tag.

**See Also:** TAG_THRESHHOLDING

,

Constant Field Values

---

#### THRESHHOLDING_RANDOMIZED_DITHER

public static final int THRESHHOLDING_RANDOMIZED_DITHER

A value to be used with the "Thresholding" tag.

TAG_CELL_WIDTH

```java
public static final int TAG_CELL_WIDTH
```

Constant specifying the "Cell_Width" tag.

**See Also:** Constant Field Values

---

#### TAG_CELL_WIDTH

public static final int TAG_CELL_WIDTH

Constant specifying the "Cell_Width" tag.

TAG_CELL_LENGTH

```java
public static final int TAG_CELL_LENGTH
```

Constant specifying the "cell_length" tag.

**See Also:** Constant Field Values

---

#### TAG_CELL_LENGTH

public static final int TAG_CELL_LENGTH

Constant specifying the "cell_length" tag.

TAG_FILL_ORDER

```java
public static final int TAG_FILL_ORDER
```

Constant specifying the "fill_order" tag.

**See Also:** FILL_ORDER_LEFT_TO_RIGHT

,

FILL_ORDER_RIGHT_TO_LEFT

,

Constant Field Values

---

#### TAG_FILL_ORDER

public static final int TAG_FILL_ORDER

Constant specifying the "fill_order" tag.

FILL_ORDER_LEFT_TO_RIGHT

```java
public static final int FILL_ORDER_LEFT_TO_RIGHT
```

A value to be used with the "FillOrder" tag.

**See Also:** TAG_FILL_ORDER

,

Constant Field Values

---

#### FILL_ORDER_LEFT_TO_RIGHT

public static final int FILL_ORDER_LEFT_TO_RIGHT

A value to be used with the "FillOrder" tag.

FILL_ORDER_RIGHT_TO_LEFT

```java
public static final int FILL_ORDER_RIGHT_TO_LEFT
```

A value to be used with the "FillOrder" tag.

**See Also:** TAG_FILL_ORDER

,

Constant Field Values

---

#### FILL_ORDER_RIGHT_TO_LEFT

public static final int FILL_ORDER_RIGHT_TO_LEFT

A value to be used with the "FillOrder" tag.

TAG_DOCUMENT_NAME

```java
public static final int TAG_DOCUMENT_NAME
```

Constant specifying the "document_name" tag.

**See Also:** Constant Field Values

---

#### TAG_DOCUMENT_NAME

public static final int TAG_DOCUMENT_NAME

Constant specifying the "document_name" tag.

TAG_IMAGE_DESCRIPTION

```java
public static final int TAG_IMAGE_DESCRIPTION
```

Constant specifying the "Image_description" tag.

**See Also:** Constant Field Values

---

#### TAG_IMAGE_DESCRIPTION

public static final int TAG_IMAGE_DESCRIPTION

Constant specifying the "Image_description" tag.

TAG_MAKE

```java
public static final int TAG_MAKE
```

Constant specifying the "Make" tag.

**See Also:** Constant Field Values

---

#### TAG_MAKE

public static final int TAG_MAKE

Constant specifying the "Make" tag.

TAG_MODEL

```java
public static final int TAG_MODEL
```

Constant specifying the "Model" tag.

**See Also:** Constant Field Values

---

#### TAG_MODEL

public static final int TAG_MODEL

Constant specifying the "Model" tag.

TAG_STRIP_OFFSETS

```java
public static final int TAG_STRIP_OFFSETS
```

Constant specifying the "Strip_offsets" tag.

**See Also:** Constant Field Values

---

#### TAG_STRIP_OFFSETS

public static final int TAG_STRIP_OFFSETS

Constant specifying the "Strip_offsets" tag.

TAG_ORIENTATION

```java
public static final int TAG_ORIENTATION
```

Constant specifying the "Orientation" tag.

**See Also:** ORIENTATION_ROW_0_TOP_COLUMN_0_LEFT

,

ORIENTATION_ROW_0_TOP_COLUMN_0_RIGHT

,

ORIENTATION_ROW_0_BOTTOM_COLUMN_0_RIGHT

,

ORIENTATION_ROW_0_BOTTOM_COLUMN_0_LEFT

,

ORIENTATION_ROW_0_LEFT_COLUMN_0_TOP

,

ORIENTATION_ROW_0_RIGHT_COLUMN_0_TOP

,

ORIENTATION_ROW_0_RIGHT_COLUMN_0_BOTTOM

,

ORIENTATION_ROW_0_LEFT_COLUMN_0_BOTTOM

,

Constant Field Values

---

#### TAG_ORIENTATION

public static final int TAG_ORIENTATION

Constant specifying the "Orientation" tag.

ORIENTATION_ROW_0_TOP_COLUMN_0_LEFT

```java
public static final int ORIENTATION_ROW_0_TOP_COLUMN_0_LEFT
```

A value to be used with the "Orientation" tag.

**See Also:** TAG_ORIENTATION

,

Constant Field Values

---

#### ORIENTATION_ROW_0_TOP_COLUMN_0_LEFT

public static final int ORIENTATION_ROW_0_TOP_COLUMN_0_LEFT

A value to be used with the "Orientation" tag.

ORIENTATION_ROW_0_TOP_COLUMN_0_RIGHT

```java
public static final int ORIENTATION_ROW_0_TOP_COLUMN_0_RIGHT
```

A value to be used with the "Orientation" tag.

**See Also:** TAG_ORIENTATION

,

Constant Field Values

---

#### ORIENTATION_ROW_0_TOP_COLUMN_0_RIGHT

public static final int ORIENTATION_ROW_0_TOP_COLUMN_0_RIGHT

A value to be used with the "Orientation" tag.

ORIENTATION_ROW_0_BOTTOM_COLUMN_0_RIGHT

```java
public static final int ORIENTATION_ROW_0_BOTTOM_COLUMN_0_RIGHT
```

A value to be used with the "Orientation" tag.

**See Also:** TAG_ORIENTATION

,

Constant Field Values

---

#### ORIENTATION_ROW_0_BOTTOM_COLUMN_0_RIGHT

public static final int ORIENTATION_ROW_0_BOTTOM_COLUMN_0_RIGHT

A value to be used with the "Orientation" tag.

ORIENTATION_ROW_0_BOTTOM_COLUMN_0_LEFT

```java
public static final int ORIENTATION_ROW_0_BOTTOM_COLUMN_0_LEFT
```

A value to be used with the "Orientation" tag.

**See Also:** TAG_ORIENTATION

,

Constant Field Values

---

#### ORIENTATION_ROW_0_BOTTOM_COLUMN_0_LEFT

public static final int ORIENTATION_ROW_0_BOTTOM_COLUMN_0_LEFT

A value to be used with the "Orientation" tag.

ORIENTATION_ROW_0_LEFT_COLUMN_0_TOP

```java
public static final int ORIENTATION_ROW_0_LEFT_COLUMN_0_TOP
```

A value to be used with the "Orientation" tag.

**See Also:** TAG_ORIENTATION

,

Constant Field Values

---

#### ORIENTATION_ROW_0_LEFT_COLUMN_0_TOP

public static final int ORIENTATION_ROW_0_LEFT_COLUMN_0_TOP

A value to be used with the "Orientation" tag.

ORIENTATION_ROW_0_RIGHT_COLUMN_0_TOP

```java
public static final int ORIENTATION_ROW_0_RIGHT_COLUMN_0_TOP
```

A value to be used with the "Orientation" tag.

**See Also:** TAG_ORIENTATION

,

Constant Field Values

---

#### ORIENTATION_ROW_0_RIGHT_COLUMN_0_TOP

public static final int ORIENTATION_ROW_0_RIGHT_COLUMN_0_TOP

A value to be used with the "Orientation" tag.

ORIENTATION_ROW_0_RIGHT_COLUMN_0_BOTTOM

```java
public static final int ORIENTATION_ROW_0_RIGHT_COLUMN_0_BOTTOM
```

A value to be used with the "Orientation" tag.

**See Also:** TAG_ORIENTATION

,

Constant Field Values

---

#### ORIENTATION_ROW_0_RIGHT_COLUMN_0_BOTTOM

public static final int ORIENTATION_ROW_0_RIGHT_COLUMN_0_BOTTOM

A value to be used with the "Orientation" tag.

ORIENTATION_ROW_0_LEFT_COLUMN_0_BOTTOM

```java
public static final int ORIENTATION_ROW_0_LEFT_COLUMN_0_BOTTOM
```

A value to be used with the "Orientation" tag.

**See Also:** TAG_ORIENTATION

,

Constant Field Values

---

#### ORIENTATION_ROW_0_LEFT_COLUMN_0_BOTTOM

public static final int ORIENTATION_ROW_0_LEFT_COLUMN_0_BOTTOM

A value to be used with the "Orientation" tag.

TAG_SAMPLES_PER_PIXEL

```java
public static final int TAG_SAMPLES_PER_PIXEL
```

Constant specifying the "Samples_per_pixel" tag.

**See Also:** Constant Field Values

---

#### TAG_SAMPLES_PER_PIXEL

public static final int TAG_SAMPLES_PER_PIXEL

Constant specifying the "Samples_per_pixel" tag.

TAG_ROWS_PER_STRIP

```java
public static final int TAG_ROWS_PER_STRIP
```

Constant specifying the "Rows_per_strip" tag.

**See Also:** Constant Field Values

---

#### TAG_ROWS_PER_STRIP

public static final int TAG_ROWS_PER_STRIP

Constant specifying the "Rows_per_strip" tag.

TAG_STRIP_BYTE_COUNTS

```java
public static final int TAG_STRIP_BYTE_COUNTS
```

Constant specifying the "Strip_byte_counts" tag.

**See Also:** Constant Field Values

---

#### TAG_STRIP_BYTE_COUNTS

public static final int TAG_STRIP_BYTE_COUNTS

Constant specifying the "Strip_byte_counts" tag.

TAG_MIN_SAMPLE_VALUE

```java
public static final int TAG_MIN_SAMPLE_VALUE
```

Constant specifying the "Min_sample_value" tag.

**See Also:** Constant Field Values

---

#### TAG_MIN_SAMPLE_VALUE

public static final int TAG_MIN_SAMPLE_VALUE

Constant specifying the "Min_sample_value" tag.

TAG_MAX_SAMPLE_VALUE

```java
public static final int TAG_MAX_SAMPLE_VALUE
```

Constant specifying the "Max_sample_value" tag.

**See Also:** Constant Field Values

---

#### TAG_MAX_SAMPLE_VALUE

public static final int TAG_MAX_SAMPLE_VALUE

Constant specifying the "Max_sample_value" tag.

TAG_X_RESOLUTION

```java
public static final int TAG_X_RESOLUTION
```

Constant specifying the "XResolution" tag.

**See Also:** Constant Field Values

---

#### TAG_X_RESOLUTION

public static final int TAG_X_RESOLUTION

Constant specifying the "XResolution" tag.

TAG_Y_RESOLUTION

```java
public static final int TAG_Y_RESOLUTION
```

Constant specifying the "YResolution" tag.

**See Also:** Constant Field Values

---

#### TAG_Y_RESOLUTION

public static final int TAG_Y_RESOLUTION

Constant specifying the "YResolution" tag.

TAG_PLANAR_CONFIGURATION

```java
public static final int TAG_PLANAR_CONFIGURATION
```

Constant specifying the "PlanarConfiguration" tag.

**See Also:** PLANAR_CONFIGURATION_CHUNKY

,

PLANAR_CONFIGURATION_PLANAR

,

Constant Field Values

---

#### TAG_PLANAR_CONFIGURATION

public static final int TAG_PLANAR_CONFIGURATION

Constant specifying the "PlanarConfiguration" tag.

PLANAR_CONFIGURATION_CHUNKY

```java
public static final int PLANAR_CONFIGURATION_CHUNKY
```

A value to be used with the "PlanarConfiguration" tag.

**See Also:** TAG_PLANAR_CONFIGURATION

,

Constant Field Values

---

#### PLANAR_CONFIGURATION_CHUNKY

public static final int PLANAR_CONFIGURATION_CHUNKY

A value to be used with the "PlanarConfiguration" tag.

PLANAR_CONFIGURATION_PLANAR

```java
public static final int PLANAR_CONFIGURATION_PLANAR
```

A value to be used with the "PlanarConfiguration" tag.

**See Also:** TAG_PLANAR_CONFIGURATION

,

Constant Field Values

---

#### PLANAR_CONFIGURATION_PLANAR

public static final int PLANAR_CONFIGURATION_PLANAR

A value to be used with the "PlanarConfiguration" tag.

TAG_PAGE_NAME

```java
public static final int TAG_PAGE_NAME
```

Constant specifying the "PageName" tag.

**See Also:** Constant Field Values

---

#### TAG_PAGE_NAME

public static final int TAG_PAGE_NAME

Constant specifying the "PageName" tag.

TAG_X_POSITION

```java
public static final int TAG_X_POSITION
```

Constant specifying the "XPosition" tag.

**See Also:** Constant Field Values

---

#### TAG_X_POSITION

public static final int TAG_X_POSITION

Constant specifying the "XPosition" tag.

TAG_Y_POSITION

```java
public static final int TAG_Y_POSITION
```

Constant specifying the "YPosition" tag.

**See Also:** Constant Field Values

---

#### TAG_Y_POSITION

public static final int TAG_Y_POSITION

Constant specifying the "YPosition" tag.

TAG_FREE_OFFSETS

```java
public static final int TAG_FREE_OFFSETS
```

Constant specifying the "FreeOffsets" tag.

**See Also:** Constant Field Values

---

#### TAG_FREE_OFFSETS

public static final int TAG_FREE_OFFSETS

Constant specifying the "FreeOffsets" tag.

TAG_FREE_BYTE_COUNTS

```java
public static final int TAG_FREE_BYTE_COUNTS
```

Constant specifying the "FreeByteCounts" tag.

**See Also:** Constant Field Values

---

#### TAG_FREE_BYTE_COUNTS

public static final int TAG_FREE_BYTE_COUNTS

Constant specifying the "FreeByteCounts" tag.

TAG_GRAY_RESPONSE_UNIT

```java
public static final int TAG_GRAY_RESPONSE_UNIT
```

Constant specifying the "GrayResponseUnit" tag.

**See Also:** GRAY_RESPONSE_UNIT_TENTHS

,

GRAY_RESPONSE_UNIT_HUNDREDTHS

,

GRAY_RESPONSE_UNIT_THOUSANDTHS

,

GRAY_RESPONSE_UNIT_TEN_THOUSANDTHS

,

GRAY_RESPONSE_UNIT_HUNDRED_THOUSANDTHS

,

Constant Field Values

---

#### TAG_GRAY_RESPONSE_UNIT

public static final int TAG_GRAY_RESPONSE_UNIT

Constant specifying the "GrayResponseUnit" tag.

GRAY_RESPONSE_UNIT_TENTHS

```java
public static final int GRAY_RESPONSE_UNIT_TENTHS
```

A value to be used with the "GrayResponseUnit" tag.

**See Also:** TAG_GRAY_RESPONSE_UNIT

,

Constant Field Values

---

#### GRAY_RESPONSE_UNIT_TENTHS

public static final int GRAY_RESPONSE_UNIT_TENTHS

A value to be used with the "GrayResponseUnit" tag.

GRAY_RESPONSE_UNIT_HUNDREDTHS

```java
public static final int GRAY_RESPONSE_UNIT_HUNDREDTHS
```

A value to be used with the "GrayResponseUnit" tag.

**See Also:** TAG_GRAY_RESPONSE_UNIT

,

Constant Field Values

---

#### GRAY_RESPONSE_UNIT_HUNDREDTHS

public static final int GRAY_RESPONSE_UNIT_HUNDREDTHS

A value to be used with the "GrayResponseUnit" tag.

GRAY_RESPONSE_UNIT_THOUSANDTHS

```java
public static final int GRAY_RESPONSE_UNIT_THOUSANDTHS
```

A value to be used with the "GrayResponseUnit" tag.

**See Also:** TAG_GRAY_RESPONSE_UNIT

,

Constant Field Values

---

#### GRAY_RESPONSE_UNIT_THOUSANDTHS

public static final int GRAY_RESPONSE_UNIT_THOUSANDTHS

A value to be used with the "GrayResponseUnit" tag.

GRAY_RESPONSE_UNIT_TEN_THOUSANDTHS

```java
public static final int GRAY_RESPONSE_UNIT_TEN_THOUSANDTHS
```

A value to be used with the "GrayResponseUnit" tag.

**See Also:** TAG_GRAY_RESPONSE_UNIT

,

Constant Field Values

---

#### GRAY_RESPONSE_UNIT_TEN_THOUSANDTHS

public static final int GRAY_RESPONSE_UNIT_TEN_THOUSANDTHS

A value to be used with the "GrayResponseUnit" tag.

GRAY_RESPONSE_UNIT_HUNDRED_THOUSANDTHS

```java
public static final int GRAY_RESPONSE_UNIT_HUNDRED_THOUSANDTHS
```

A value to be used with the "GrayResponseUnit" tag.

**See Also:** TAG_GRAY_RESPONSE_UNIT

,

Constant Field Values

---

#### GRAY_RESPONSE_UNIT_HUNDRED_THOUSANDTHS

public static final int GRAY_RESPONSE_UNIT_HUNDRED_THOUSANDTHS

A value to be used with the "GrayResponseUnit" tag.

TAG_GRAY_RESPONSE_CURVE

```java
public static final int TAG_GRAY_RESPONSE_CURVE
```

Constant specifying the "GrayResponseCurve" tag.

**See Also:** Constant Field Values

---

#### TAG_GRAY_RESPONSE_CURVE

public static final int TAG_GRAY_RESPONSE_CURVE

Constant specifying the "GrayResponseCurve" tag.

TAG_T4_OPTIONS

```java
public static final int TAG_T4_OPTIONS
```

Constant specifying the "T4Options" tag.

**See Also:** T4_OPTIONS_2D_CODING

,

T4_OPTIONS_UNCOMPRESSED

,

T4_OPTIONS_EOL_BYTE_ALIGNED

,

Constant Field Values

---

#### TAG_T4_OPTIONS

public static final int TAG_T4_OPTIONS

Constant specifying the "T4Options" tag.

T4_OPTIONS_2D_CODING

```java
public static final int T4_OPTIONS_2D_CODING
```

A mask to be used with the "T4Options" tag.

**See Also:** TAG_T4_OPTIONS

,

Constant Field Values

---

#### T4_OPTIONS_2D_CODING

public static final int T4_OPTIONS_2D_CODING

A mask to be used with the "T4Options" tag.

T4_OPTIONS_UNCOMPRESSED

```java
public static final int T4_OPTIONS_UNCOMPRESSED
```

A mask to be used with the "T4Options" tag.

**See Also:** TAG_T4_OPTIONS

,

Constant Field Values

---

#### T4_OPTIONS_UNCOMPRESSED

public static final int T4_OPTIONS_UNCOMPRESSED

A mask to be used with the "T4Options" tag.

T4_OPTIONS_EOL_BYTE_ALIGNED

```java
public static final int T4_OPTIONS_EOL_BYTE_ALIGNED
```

A mask to be used with the "T4Options" tag.

**See Also:** TAG_T4_OPTIONS

,

Constant Field Values

---

#### T4_OPTIONS_EOL_BYTE_ALIGNED

public static final int T4_OPTIONS_EOL_BYTE_ALIGNED

A mask to be used with the "T4Options" tag.

TAG_T6_OPTIONS

```java
public static final int TAG_T6_OPTIONS
```

Constant specifying the "T6Options" tag.

**See Also:** T6_OPTIONS_UNCOMPRESSED

,

Constant Field Values

---

#### TAG_T6_OPTIONS

public static final int TAG_T6_OPTIONS

Constant specifying the "T6Options" tag.

T6_OPTIONS_UNCOMPRESSED

```java
public static final int T6_OPTIONS_UNCOMPRESSED
```

A mask to be used with the "T6Options" tag.

**See Also:** TAG_T6_OPTIONS

,

Constant Field Values

---

#### T6_OPTIONS_UNCOMPRESSED

public static final int T6_OPTIONS_UNCOMPRESSED

A mask to be used with the "T6Options" tag.

TAG_RESOLUTION_UNIT

```java
public static final int TAG_RESOLUTION_UNIT
```

Constant specifying the "ResolutionUnit" tag.

**See Also:** RESOLUTION_UNIT_NONE

,

RESOLUTION_UNIT_INCH

,

RESOLUTION_UNIT_CENTIMETER

,

Constant Field Values

---

#### TAG_RESOLUTION_UNIT

public static final int TAG_RESOLUTION_UNIT

Constant specifying the "ResolutionUnit" tag.

RESOLUTION_UNIT_NONE

```java
public static final int RESOLUTION_UNIT_NONE
```

A value to be used with the "ResolutionUnit" tag.

**See Also:** TAG_RESOLUTION_UNIT

,

Constant Field Values

---

#### RESOLUTION_UNIT_NONE

public static final int RESOLUTION_UNIT_NONE

A value to be used with the "ResolutionUnit" tag.

RESOLUTION_UNIT_INCH

```java
public static final int RESOLUTION_UNIT_INCH
```

A value to be used with the "ResolutionUnit" tag.

**See Also:** TAG_RESOLUTION_UNIT

,

Constant Field Values

---

#### RESOLUTION_UNIT_INCH

public static final int RESOLUTION_UNIT_INCH

A value to be used with the "ResolutionUnit" tag.

RESOLUTION_UNIT_CENTIMETER

```java
public static final int RESOLUTION_UNIT_CENTIMETER
```

A value to be used with the "ResolutionUnit" tag.

**See Also:** TAG_RESOLUTION_UNIT

,

Constant Field Values

---

#### RESOLUTION_UNIT_CENTIMETER

public static final int RESOLUTION_UNIT_CENTIMETER

A value to be used with the "ResolutionUnit" tag.

TAG_PAGE_NUMBER

```java
public static final int TAG_PAGE_NUMBER
```

Constant specifying the "PageNumber" tag.

**See Also:** Constant Field Values

---

#### TAG_PAGE_NUMBER

public static final int TAG_PAGE_NUMBER

Constant specifying the "PageNumber" tag.

TAG_TRANSFER_FUNCTION

```java
public static final int TAG_TRANSFER_FUNCTION
```

Constant specifying the "TransferFunction" tag.

**See Also:** Constant Field Values

---

#### TAG_TRANSFER_FUNCTION

public static final int TAG_TRANSFER_FUNCTION

Constant specifying the "TransferFunction" tag.

TAG_SOFTWARE

```java
public static final int TAG_SOFTWARE
```

Constant specifying the "Software" tag.

**See Also:** Constant Field Values

---

#### TAG_SOFTWARE

public static final int TAG_SOFTWARE

Constant specifying the "Software" tag.

TAG_DATE_TIME

```java
public static final int TAG_DATE_TIME
```

Constant specifying the "DateTime" tag.

**See Also:** Constant Field Values

---

#### TAG_DATE_TIME

public static final int TAG_DATE_TIME

Constant specifying the "DateTime" tag.

TAG_ARTIST

```java
public static final int TAG_ARTIST
```

Constant specifying the "Artist" tag.

**See Also:** Constant Field Values

---

#### TAG_ARTIST

public static final int TAG_ARTIST

Constant specifying the "Artist" tag.

TAG_HOST_COMPUTER

```java
public static final int TAG_HOST_COMPUTER
```

Constant specifying the "HostComputer" tag.

**See Also:** Constant Field Values

---

#### TAG_HOST_COMPUTER

public static final int TAG_HOST_COMPUTER

Constant specifying the "HostComputer" tag.

TAG_PREDICTOR

```java
public static final int TAG_PREDICTOR
```

Constant specifying the "Predictor" tag.

**See Also:** TAG_WHITE_POINT

,

TAG_PRIMARY_CHROMATICITES

,

TAG_COLOR_MAP

,

TAG_HALFTONE_HINTS

,

TAG_TILE_WIDTH

,

TAG_TILE_LENGTH

,

TAG_TILE_OFFSETS

,

TAG_TILE_BYTE_COUNTS

,

Constant Field Values

---

#### TAG_PREDICTOR

public static final int TAG_PREDICTOR

Constant specifying the "Predictor" tag.

PREDICTOR_NONE

```java
public static final int PREDICTOR_NONE
```

A value to be used with the "Predictor" tag.

**See Also:** TAG_PREDICTOR

,

Constant Field Values

---

#### PREDICTOR_NONE

public static final int PREDICTOR_NONE

A value to be used with the "Predictor" tag.

PREDICTOR_HORIZONTAL_DIFFERENCING

```java
public static final int PREDICTOR_HORIZONTAL_DIFFERENCING
```

A value to be used with the "Predictor" tag.

**See Also:** TAG_PREDICTOR

,

Constant Field Values

---

#### PREDICTOR_HORIZONTAL_DIFFERENCING

public static final int PREDICTOR_HORIZONTAL_DIFFERENCING

A value to be used with the "Predictor" tag.

TAG_WHITE_POINT

```java
public static final int TAG_WHITE_POINT
```

Constant specifying the "WhitePoint" tag.

**See Also:** Constant Field Values

---

#### TAG_WHITE_POINT

public static final int TAG_WHITE_POINT

Constant specifying the "WhitePoint" tag.

TAG_PRIMARY_CHROMATICITES

```java
public static final int TAG_PRIMARY_CHROMATICITES
```

Constant specifying the "PrimaryChromaticites" tag.

**See Also:** Constant Field Values

---

#### TAG_PRIMARY_CHROMATICITES

public static final int TAG_PRIMARY_CHROMATICITES

Constant specifying the "PrimaryChromaticites" tag.

TAG_COLOR_MAP

```java
public static final int TAG_COLOR_MAP
```

Constant specifying the "ColorMap" tag.

**See Also:** Constant Field Values

---

#### TAG_COLOR_MAP

public static final int TAG_COLOR_MAP

Constant specifying the "ColorMap" tag.

TAG_HALFTONE_HINTS

```java
public static final int TAG_HALFTONE_HINTS
```

Constant specifying the "HalftoneHints" tag.

**See Also:** Constant Field Values

---

#### TAG_HALFTONE_HINTS

public static final int TAG_HALFTONE_HINTS

Constant specifying the "HalftoneHints" tag.

TAG_TILE_WIDTH

```java
public static final int TAG_TILE_WIDTH
```

Constant specifying the "TileWidth" tag.

**See Also:** Constant Field Values

---

#### TAG_TILE_WIDTH

public static final int TAG_TILE_WIDTH

Constant specifying the "TileWidth" tag.

TAG_TILE_LENGTH

```java
public static final int TAG_TILE_LENGTH
```

Constant specifying the "TileLength" tag.

**See Also:** Constant Field Values

---

#### TAG_TILE_LENGTH

public static final int TAG_TILE_LENGTH

Constant specifying the "TileLength" tag.

TAG_TILE_OFFSETS

```java
public static final int TAG_TILE_OFFSETS
```

Constant specifying the "TileOffsets" tag.

**See Also:** Constant Field Values

---

#### TAG_TILE_OFFSETS

public static final int TAG_TILE_OFFSETS

Constant specifying the "TileOffsets" tag.

TAG_TILE_BYTE_COUNTS

```java
public static final int TAG_TILE_BYTE_COUNTS
```

Constant specifying the "TileByteCounts" tag.

**See Also:** Constant Field Values

---

#### TAG_TILE_BYTE_COUNTS

public static final int TAG_TILE_BYTE_COUNTS

Constant specifying the "TileByteCounts" tag.

TAG_INK_SET

```java
public static final int TAG_INK_SET
```

Constant specifying the "InkSet" tag.

**See Also:** INK_SET_CMYK

,

INK_SET_NOT_CMYK

,

Constant Field Values

---

#### TAG_INK_SET

public static final int TAG_INK_SET

Constant specifying the "InkSet" tag.

INK_SET_CMYK

```java
public static final int INK_SET_CMYK
```

A value to be used with the "InkSet" tag.

**See Also:** TAG_INK_SET

,

Constant Field Values

---

#### INK_SET_CMYK

public static final int INK_SET_CMYK

A value to be used with the "InkSet" tag.

INK_SET_NOT_CMYK

```java
public static final int INK_SET_NOT_CMYK
```

A value to be used with the "InkSet" tag.

**See Also:** TAG_INK_SET

,

Constant Field Values

---

#### INK_SET_NOT_CMYK

public static final int INK_SET_NOT_CMYK

A value to be used with the "InkSet" tag.

TAG_INK_NAMES

```java
public static final int TAG_INK_NAMES
```

Constant specifying the "InkNames" tag.

**See Also:** Constant Field Values

---

#### TAG_INK_NAMES

public static final int TAG_INK_NAMES

Constant specifying the "InkNames" tag.

TAG_NUMBER_OF_INKS

```java
public static final int TAG_NUMBER_OF_INKS
```

Constant specifying the "NumberOfInks" tag.

**See Also:** Constant Field Values

---

#### TAG_NUMBER_OF_INKS

public static final int TAG_NUMBER_OF_INKS

Constant specifying the "NumberOfInks" tag.

TAG_DOT_RANGE

```java
public static final int TAG_DOT_RANGE
```

Constant specifying the "DotRange" tag.

**See Also:** Constant Field Values

---

#### TAG_DOT_RANGE

public static final int TAG_DOT_RANGE

Constant specifying the "DotRange" tag.

TAG_TARGET_PRINTER

```java
public static final int TAG_TARGET_PRINTER
```

Constant specifying the "TargetPrinter" tag.

**See Also:** Constant Field Values

---

#### TAG_TARGET_PRINTER

public static final int TAG_TARGET_PRINTER

Constant specifying the "TargetPrinter" tag.

TAG_EXTRA_SAMPLES

```java
public static final int TAG_EXTRA_SAMPLES
```

Constant specifying the "ExtraSamples" tag.

**See Also:** EXTRA_SAMPLES_UNSPECIFIED

,

EXTRA_SAMPLES_ASSOCIATED_ALPHA

,

EXTRA_SAMPLES_UNASSOCIATED_ALPHA

,

Constant Field Values

---

#### TAG_EXTRA_SAMPLES

public static final int TAG_EXTRA_SAMPLES

Constant specifying the "ExtraSamples" tag.

EXTRA_SAMPLES_UNSPECIFIED

```java
public static final int EXTRA_SAMPLES_UNSPECIFIED
```

A value to be used with the "ExtraSamples" tag.

**See Also:** TAG_EXTRA_SAMPLES

,

Constant Field Values

---

#### EXTRA_SAMPLES_UNSPECIFIED

public static final int EXTRA_SAMPLES_UNSPECIFIED

A value to be used with the "ExtraSamples" tag.

EXTRA_SAMPLES_ASSOCIATED_ALPHA

```java
public static final int EXTRA_SAMPLES_ASSOCIATED_ALPHA
```

A value to be used with the "ExtraSamples" tag.

**See Also:** TAG_EXTRA_SAMPLES

,

Constant Field Values

---

#### EXTRA_SAMPLES_ASSOCIATED_ALPHA

public static final int EXTRA_SAMPLES_ASSOCIATED_ALPHA

A value to be used with the "ExtraSamples" tag.

EXTRA_SAMPLES_UNASSOCIATED_ALPHA

```java
public static final int EXTRA_SAMPLES_UNASSOCIATED_ALPHA
```

A value to be used with the "ExtraSamples" tag.

**See Also:** TAG_EXTRA_SAMPLES

,

Constant Field Values

---

#### EXTRA_SAMPLES_UNASSOCIATED_ALPHA

public static final int EXTRA_SAMPLES_UNASSOCIATED_ALPHA

A value to be used with the "ExtraSamples" tag.

TAG_SAMPLE_FORMAT

```java
public static final int TAG_SAMPLE_FORMAT
```

Constant specifying the "SampleFormat" tag.

**See Also:** SAMPLE_FORMAT_UNSIGNED_INTEGER

,

SAMPLE_FORMAT_SIGNED_INTEGER

,

SAMPLE_FORMAT_FLOATING_POINT

,

SAMPLE_FORMAT_UNDEFINED

,

Constant Field Values

---

#### TAG_SAMPLE_FORMAT

public static final int TAG_SAMPLE_FORMAT

Constant specifying the "SampleFormat" tag.

SAMPLE_FORMAT_UNSIGNED_INTEGER

```java
public static final int SAMPLE_FORMAT_UNSIGNED_INTEGER
```

A value to be used with the "SampleFormat" tag.

**See Also:** TAG_SAMPLE_FORMAT

,

Constant Field Values

---

#### SAMPLE_FORMAT_UNSIGNED_INTEGER

public static final int SAMPLE_FORMAT_UNSIGNED_INTEGER

A value to be used with the "SampleFormat" tag.

SAMPLE_FORMAT_SIGNED_INTEGER

```java
public static final int SAMPLE_FORMAT_SIGNED_INTEGER
```

A value to be used with the "SampleFormat" tag.

**See Also:** TAG_SAMPLE_FORMAT

,

Constant Field Values

---

#### SAMPLE_FORMAT_SIGNED_INTEGER

public static final int SAMPLE_FORMAT_SIGNED_INTEGER

A value to be used with the "SampleFormat" tag.

SAMPLE_FORMAT_FLOATING_POINT

```java
public static final int SAMPLE_FORMAT_FLOATING_POINT
```

A value to be used with the "SampleFormat" tag.

**See Also:** TAG_SAMPLE_FORMAT

,

Constant Field Values

---

#### SAMPLE_FORMAT_FLOATING_POINT

public static final int SAMPLE_FORMAT_FLOATING_POINT

A value to be used with the "SampleFormat" tag.

SAMPLE_FORMAT_UNDEFINED

```java
public static final int SAMPLE_FORMAT_UNDEFINED
```

A value to be used with the "SampleFormat" tag.

**See Also:** TAG_SAMPLE_FORMAT

,

Constant Field Values

---

#### SAMPLE_FORMAT_UNDEFINED

public static final int SAMPLE_FORMAT_UNDEFINED

A value to be used with the "SampleFormat" tag.

TAG_S_MIN_SAMPLE_VALUE

```java
public static final int TAG_S_MIN_SAMPLE_VALUE
```

Constant specifying the "SMinSampleValue" tag.

**See Also:** Constant Field Values

---

#### TAG_S_MIN_SAMPLE_VALUE

public static final int TAG_S_MIN_SAMPLE_VALUE

Constant specifying the "SMinSampleValue" tag.

TAG_S_MAX_SAMPLE_VALUE

```java
public static final int TAG_S_MAX_SAMPLE_VALUE
```

Constant specifying the "SMaxSampleValue" tag.

**See Also:** Constant Field Values

---

#### TAG_S_MAX_SAMPLE_VALUE

public static final int TAG_S_MAX_SAMPLE_VALUE

Constant specifying the "SMaxSampleValue" tag.

TAG_TRANSFER_RANGE

```java
public static final int TAG_TRANSFER_RANGE
```

Constant specifying the "TransferRange" tag.

**See Also:** Constant Field Values

---

#### TAG_TRANSFER_RANGE

public static final int TAG_TRANSFER_RANGE

Constant specifying the "TransferRange" tag.

TAG_JPEG_TABLES

```java
public static final int TAG_JPEG_TABLES
```

Constant specifying the "JPEGTables" tag.

**See Also:** JPEG-in-TIFF compression

,

Constant Field Values

---

#### TAG_JPEG_TABLES

public static final int TAG_JPEG_TABLES

Constant specifying the "JPEGTables" tag.

TAG_JPEG_PROC

```java
public static final int TAG_JPEG_PROC
```

Constant specifying the "JPEGProc" tag.

**See Also:** Constant Field Values

---

#### TAG_JPEG_PROC

public static final int TAG_JPEG_PROC

Constant specifying the "JPEGProc" tag.

JPEG_PROC_BASELINE

```java
public static final int JPEG_PROC_BASELINE
```

A value to be used with the "JPEGProc" tag.

**See Also:** TAG_JPEG_PROC

,

Constant Field Values

---

#### JPEG_PROC_BASELINE

public static final int JPEG_PROC_BASELINE

A value to be used with the "JPEGProc" tag.

JPEG_PROC_LOSSLESS

```java
public static final int JPEG_PROC_LOSSLESS
```

A value to be used with the "JPEGProc" tag.

**See Also:** TAG_JPEG_PROC

,

Constant Field Values

---

#### JPEG_PROC_LOSSLESS

public static final int JPEG_PROC_LOSSLESS

A value to be used with the "JPEGProc" tag.

TAG_JPEG_INTERCHANGE_FORMAT

```java
public static final int TAG_JPEG_INTERCHANGE_FORMAT
```

Constant specifying the "JPEGInterchangeFormat" tag.

**See Also:** Constant Field Values

---

#### TAG_JPEG_INTERCHANGE_FORMAT

public static final int TAG_JPEG_INTERCHANGE_FORMAT

Constant specifying the "JPEGInterchangeFormat" tag.

TAG_JPEG_INTERCHANGE_FORMAT_LENGTH

```java
public static final int TAG_JPEG_INTERCHANGE_FORMAT_LENGTH
```

Constant specifying the "JPEGInterchangeFormatLength" tag.

**See Also:** Constant Field Values

---

#### TAG_JPEG_INTERCHANGE_FORMAT_LENGTH

public static final int TAG_JPEG_INTERCHANGE_FORMAT_LENGTH

Constant specifying the "JPEGInterchangeFormatLength" tag.

TAG_JPEG_RESTART_INTERVAL

```java
public static final int TAG_JPEG_RESTART_INTERVAL
```

Constant specifying the "JPEGRestartInterval" tag.

**See Also:** Constant Field Values

---

#### TAG_JPEG_RESTART_INTERVAL

public static final int TAG_JPEG_RESTART_INTERVAL

Constant specifying the "JPEGRestartInterval" tag.

TAG_JPEG_LOSSLESS_PREDICTORS

```java
public static final int TAG_JPEG_LOSSLESS_PREDICTORS
```

Constant specifying the "JPEGLosslessPredictors" tag.

**See Also:** Constant Field Values

---

#### TAG_JPEG_LOSSLESS_PREDICTORS

public static final int TAG_JPEG_LOSSLESS_PREDICTORS

Constant specifying the "JPEGLosslessPredictors" tag.

TAG_JPEG_POINT_TRANSFORMS

```java
public static final int TAG_JPEG_POINT_TRANSFORMS
```

Constant specifying the "JPEGPointTransforms" tag.

**See Also:** Constant Field Values

---

#### TAG_JPEG_POINT_TRANSFORMS

public static final int TAG_JPEG_POINT_TRANSFORMS

Constant specifying the "JPEGPointTransforms" tag.

TAG_JPEG_Q_TABLES

```java
public static final int TAG_JPEG_Q_TABLES
```

Constant specifying the "JPEGQTables" tag.

**See Also:** Constant Field Values

---

#### TAG_JPEG_Q_TABLES

public static final int TAG_JPEG_Q_TABLES

Constant specifying the "JPEGQTables" tag.

TAG_JPEG_DC_TABLES

```java
public static final int TAG_JPEG_DC_TABLES
```

Constant specifying the "JPEGDCTables" tag.

**See Also:** Constant Field Values

---

#### TAG_JPEG_DC_TABLES

public static final int TAG_JPEG_DC_TABLES

Constant specifying the "JPEGDCTables" tag.

TAG_JPEG_AC_TABLES

```java
public static final int TAG_JPEG_AC_TABLES
```

Constant specifying the "JPEGACTables" tag.

**See Also:** Constant Field Values

---

#### TAG_JPEG_AC_TABLES

public static final int TAG_JPEG_AC_TABLES

Constant specifying the "JPEGACTables" tag.

TAG_Y_CB_CR_COEFFICIENTS

```java
public static final int TAG_Y_CB_CR_COEFFICIENTS
```

Constant specifying the "YCbCrCoefficients" tag.

**See Also:** Constant Field Values

---

#### TAG_Y_CB_CR_COEFFICIENTS

public static final int TAG_Y_CB_CR_COEFFICIENTS

Constant specifying the "YCbCrCoefficients" tag.

TAG_Y_CB_CR_SUBSAMPLING

```java
public static final int TAG_Y_CB_CR_SUBSAMPLING
```

Constant specifying the "YCbCrSubsampling" tag.

**See Also:** Constant Field Values

---

#### TAG_Y_CB_CR_SUBSAMPLING

public static final int TAG_Y_CB_CR_SUBSAMPLING

Constant specifying the "YCbCrSubsampling" tag.

TAG_Y_CB_CR_POSITIONING

```java
public static final int TAG_Y_CB_CR_POSITIONING
```

Constant specifying the "YCbCrPositioning" tag.

**See Also:** Y_CB_CR_POSITIONING_CENTERED

,

Y_CB_CR_POSITIONING_COSITED

,

Constant Field Values

---

#### TAG_Y_CB_CR_POSITIONING

public static final int TAG_Y_CB_CR_POSITIONING

Constant specifying the "YCbCrPositioning" tag.

Y_CB_CR_POSITIONING_CENTERED

```java
public static final int Y_CB_CR_POSITIONING_CENTERED
```

A value to be used with the "YCbCrPositioning" tag.

**See Also:** TAG_Y_CB_CR_POSITIONING

,

Constant Field Values

---

#### Y_CB_CR_POSITIONING_CENTERED

public static final int Y_CB_CR_POSITIONING_CENTERED

A value to be used with the "YCbCrPositioning" tag.

Y_CB_CR_POSITIONING_COSITED

```java
public static final int Y_CB_CR_POSITIONING_COSITED
```

A value to be used with the "YCbCrPositioning" tag.

**See Also:** TAG_Y_CB_CR_POSITIONING

,

Constant Field Values

---

#### Y_CB_CR_POSITIONING_COSITED

public static final int Y_CB_CR_POSITIONING_COSITED

A value to be used with the "YCbCrPositioning" tag.

TAG_REFERENCE_BLACK_WHITE

```java
public static final int TAG_REFERENCE_BLACK_WHITE
```

Constant specifying the "ReferenceBlackWhite" tag.

**See Also:** Constant Field Values

---

#### TAG_REFERENCE_BLACK_WHITE

public static final int TAG_REFERENCE_BLACK_WHITE

Constant specifying the "ReferenceBlackWhite" tag.

TAG_COPYRIGHT

```java
public static final int TAG_COPYRIGHT
```

Constant specifying the "Copyright" tag.

**See Also:** Constant Field Values

---

#### TAG_COPYRIGHT

public static final int TAG_COPYRIGHT

Constant specifying the "Copyright" tag.

TAG_ICC_PROFILE

```java
public static final int TAG_ICC_PROFILE
```

Constant specifying the "ICC Profile" tag.

**See Also:** ICC Specification, section B.4: Embedding ICC profiles in TIFF files

,

Constant Field Values

---

#### TAG_ICC_PROFILE

public static final int TAG_ICC_PROFILE

Constant specifying the "ICC Profile" tag.

Method Detail

- getInstance

```java
public static
BaselineTIFFTagSet
getInstance()
```

Returns a shared instance of a

BaselineTIFFTagSet

.

**Returns:** a

BaselineTIFFTagSet

instance.

---

#### Method Detail

getInstance

```java
public static
BaselineTIFFTagSet
getInstance()
```

Returns a shared instance of a

BaselineTIFFTagSet

.

**Returns:** a

BaselineTIFFTagSet

instance.

---

#### getInstance

public static

BaselineTIFFTagSet

getInstance()

Returns a shared instance of a

BaselineTIFFTagSet

.

---

