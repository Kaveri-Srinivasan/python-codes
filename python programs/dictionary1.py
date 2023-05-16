def replace_numeric_keys(obj):
    if isinstance(obj, dict):
        new_dict = {}
        for key, value in obj.items():
            if isinstance(key, str):
                key = ''.join('_' if c.isdigit() else c for c in key)
            new_dict[key] = replace_numeric_keys(value)
        return new_dict
    elif isinstance(obj, list):
        new_list = []
        for item in obj:
            new_list.append(replace_numeric_keys(item))
        return new_list
    else:
        return obj
original_dict = {
    "objectives1111": "CONVERSIONS",
    "actions": [{
        "action_device11111": "android_smartphone",
        "action_type": "offsite_coversion.fb_pixel_view_content",
        "28d_click": "1",
        "34d_data": {
            "ratio": "3.4",
            "45data_insight": True
        }
    },
    {
        "action_device": "android_smartphone",
        "action_type": "omni_view_content",
        "28d_click": "1"
    },
    {
        "action_device": "android_smartphone",
        "action_type": "view_content",
        "28d_click": "1"
    }],
    "8986ad_id": 231341,
    "34date_start": "2021-02-21",
    "date-stop": "2021-02-21",
    "action_values": [{
        "action_device": "android_smartphone",
        "action_type": "offsite_conversion.fb_pixel_view_content",
        "28d_click": "9.99"
    },
    {
        "action_device": "android_smartphone",
        "action_type": "omni_view_content",
        "28d_click": "9.99"
    }],
    "platform_position": "feed"
}

new_dict = replace_numeric_keys(original_dict)
print(new_dict)


