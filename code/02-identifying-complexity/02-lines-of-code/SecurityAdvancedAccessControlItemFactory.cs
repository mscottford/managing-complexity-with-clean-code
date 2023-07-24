// This file copied in full from the Files project. It was retrieved from 
// https://github.com/files-community/Files/blob/c740d5714e6cdbd4e67a05e2cfd1b083c1106e8f/src/Files.App/Data/Factories/SecurityAdvancedAccessControlItemFactory.cs
// on July 23, 2023. The file was licensed under the MIT license, 
// which is reproduced below.

// Copyright (c) 2023 Files Community
// Licensed under the MIT License. See the LICENSE.

using Files.App.Extensions;
using System.Collections.Generic;
using System.Collections.ObjectModel;

namespace Files.App.Data.Factories
{
    public static class SecurityAdvancedAccessControlItemFactory
    {
        // This function has 185 lines of code. It contains 4 lines that
        // contain only whitespace.

        /// <summary>
        /// Returned list list will be shown in an ACE item in security advanced page
        /// </summary>
        /// <param name="current"></param>
        /// <param name="isAdvanced"></param>
        /// <param name="isInherited"></param>
        /// <param name="isFolder"></param>
        /// <returns></returns>
        public static ObservableCollection<AccessMaskItem> Initialize(AccessControlEntry current, bool isAdvanced, bool isInherited, bool isFolder)
        {
            List<AccessMaskItem> accessControls;

            if (isAdvanced)
            {
                accessControls = new()
                {
                    new(current)
                    {
                        AccessMask = AccessMaskFlags.FullControl,
                        AccessMaskName = "SecurityFullControlLabel/Text".GetLocalizedResource(),
                        IsEditable = !isInherited
                    },
                    new(current)
                    {
                        AccessMask = AccessMaskFlags.Traverse,
                        AccessMaskName = "SecurityTraverseLabel/Text".GetLocalizedResource(),
                        IsEditable = !isInherited
                    },
                    new(current)
                    {
                        AccessMask = AccessMaskFlags.ExecuteFile,
                        AccessMaskName = "SecurityExecuteFileLabel/Text".GetLocalizedResource(),
                        IsEditable = !isInherited
                    },
                    new(current)
                    {
                        AccessMask = AccessMaskFlags.ListDirectory,
                        AccessMaskName = "SecurityListDirectoryLabel/Text".GetLocalizedResource(),
                        IsEditable = !isInherited
                    },
                    new(current)
                    {
                        AccessMask = AccessMaskFlags.ReadData,
                        AccessMaskName = "SecurityReadDataLabel/Text".GetLocalizedResource(),
                        IsEditable = !isInherited
                    },
                    new(current)
                    {
                        AccessMask = AccessMaskFlags.ReadAttributes,
                        AccessMaskName = "SecurityReadAttributesLabel/Text".GetLocalizedResource(),
                        IsEditable = !isInherited
                    },
                    new(current)
                    {
                        AccessMask = AccessMaskFlags.ReadExtendedAttributes,
                        AccessMaskName = "SecurityReadExtendedAttributesLabel/Text".GetLocalizedResource(),
                        IsEditable = !isInherited
                    },
                    new(current)
                    {
                        AccessMask = AccessMaskFlags.CreateFiles,
                        AccessMaskName = "SecurityCreateFilesLabel/Text".GetLocalizedResource(),
                        IsEditable = !isInherited
                    },
                    new(current)
                    {
                        AccessMask = AccessMaskFlags.CreateDirectories,
                        AccessMaskName = "SecurityCreateDirectoriesLabel/Text".GetLocalizedResource(),
                        IsEditable = !isInherited
                    },
                    new(current)
                    {
                        AccessMask = AccessMaskFlags.WriteData,
                        AccessMaskName = "SecurityWriteDataLabel/Text".GetLocalizedResource(),
                        IsEditable = !isInherited
                    },
                    new(current)
                    {
                        AccessMask = AccessMaskFlags.AppendData,
                        AccessMaskName = "SecurityAppendDataLabel/Text".GetLocalizedResource(),
                        IsEditable = !isInherited
                    },
                    new(current)
                    {
                        AccessMask = AccessMaskFlags.WriteAttributes,
                        AccessMaskName = "SecurityWriteAttributesLabel/Text".GetLocalizedResource(),
                        IsEditable = !isInherited
                    },
                    new(current)
                    {
                        AccessMask = AccessMaskFlags.WriteExtendedAttributes,
                        AccessMaskName = "SecurityWriteExtendedAttributesLabel/Text".GetLocalizedResource(),
                        IsEditable = !isInherited
                    },
                    new(current)
                    {
                        AccessMask = AccessMaskFlags.DeleteSubdirectoriesAndFiles,
                        AccessMaskName = "SecurityDeleteSubdirectoriesAndFilesLabel/Text".GetLocalizedResource(),
                        IsEditable = !isInherited
                    },
                    new(current)
                    {
                        AccessMask = AccessMaskFlags.Delete,
                        AccessMaskName = "Delete".GetLocalizedResource(),
                        IsEditable = !isInherited
                    },
                    new(current)
                    {
                        AccessMask = AccessMaskFlags.ReadPermissions,
                        AccessMaskName = "SecurityReadPermissionsLabel/Text".GetLocalizedResource(),
                        IsEditable = !isInherited
                    },
                    new(current)
                    {
                        AccessMask = AccessMaskFlags.ChangePermissions,
                        AccessMaskName = "SecurityChangePermissionsLabel/Text".GetLocalizedResource(),
                        IsEditable = !isInherited
                    },
                    new(current)
                    {
                        AccessMask = AccessMaskFlags.TakeOwnership,
                        AccessMaskName = "SecurityTakeOwnershipLabel/Text".GetLocalizedResource(),
                        IsEditable = !isInherited
                    }
                };

                if (isFolder)
                {
                    accessControls.RemoveAll(x =>
                        x.AccessMask == AccessMaskFlags.ExecuteFile ||
                        x.AccessMask == AccessMaskFlags.ReadData ||
                        x.AccessMask == AccessMaskFlags.WriteData ||
                        x.AccessMask == AccessMaskFlags.AppendData);
                }
                else
                {
                    accessControls.RemoveAll(x =>
                        x.AccessMask == AccessMaskFlags.Traverse ||
                        x.AccessMask == AccessMaskFlags.ListDirectory ||
                        x.AccessMask == AccessMaskFlags.CreateFiles ||
                        x.AccessMask == AccessMaskFlags.CreateDirectories ||
                        x.AccessMask == AccessMaskFlags.DeleteSubdirectoriesAndFiles);
                }
            }
            else
            {
                accessControls = new()
                {
                    new(current)
                    {
                        AccessMask = AccessMaskFlags.FullControl,
                        AccessMaskName = "SecurityFullControlLabel/Text".GetLocalizedResource(),
                        IsEditable = !isInherited
                    },
                    new(current)
                    {
                        AccessMask = AccessMaskFlags.Modify,
                        AccessMaskName = "SecurityModifyLabel/Text".GetLocalizedResource(),
                        IsEditable = !isInherited
                    },
                    new(current)
                    {
                        AccessMask = AccessMaskFlags.ReadAndExecute,
                        AccessMaskName = "SecurityReadAndExecuteLabel/Text".GetLocalizedResource(),
                        IsEditable = !isInherited
                    },
                    new(current)
                    {
                        AccessMask = AccessMaskFlags.ListDirectory,
                        AccessMaskName = "SecurityListDirectoryLabel/Text".GetLocalizedResource(),
                        IsEditable = !isInherited
                    },
                    new(current)
                    {
                        AccessMask = AccessMaskFlags.Read,
                        AccessMaskName = "SecurityReadLabel/Text".GetLocalizedResource(),
                        IsEditable = !isInherited
                    },
                    new(current)
                    {
                        AccessMask = AccessMaskFlags.Write,
                        AccessMaskName = "Write".GetLocalizedResource(),
                        IsEditable = !isInherited
                    },
                    new(current, false)
                    {
                        AccessMaskName = "SecuritySpecialLabel/Text".GetLocalizedResource()
                    }
                };

                if (!isFolder)
                {
                    accessControls.RemoveAll(x =>
                        x.AccessMask == AccessMaskFlags.ListDirectory);
                }
            }

            return new ObservableCollection<AccessMaskItem>(accessControls);
        }
    }
}

// The license below was copied from https://github.com/files-community/Files/blob/c740d5714e6cdbd4e67a05e2cfd1b083c1106e8f/LICENSE.
//
// MIT License
//
// Copyright (c) 2023 Files Community
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.
