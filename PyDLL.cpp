extern "C" _declspec(dllexport) int combo(int arr[15][15], int x, int y)
{
	int x_left = x - 4 < 0 ? 0 : x - 4;
	int y_left = y - 4 < 0 ? 0 : y - 4;
	int x_right = x + 4 > 14 ? 14 : x + 4;
	int y_right = y + 4 > 14 ? 14 : y + 4;

	int value = arr[x][y];
	int max = 1;
	int i, j, k, count = 0;

	for (i = x_left; i <= x_right; i++)
	{
		if (arr[i][y] == value)
		{
			count++;
			if (count > max)
			{
				max = count;
				if (max == 5)
				{
					return max;
				}
			}
		}
		else
		{
			count = 0;
		}
	}

	count = 0;

	for (j = y_left; j <= y_right; j++)
	{
		if (arr[x][j] == value)
		{
			count++;
			if (count > max)
			{
				max = count;
				if (max == 5)
				{
					return max;
				}
			}
		}
		else
		{
			count = 0;
		}
	}

	count = 0;

	for (k = -4; k <= 4; k++)
	{
		i = x + k;
		j = y + k;
		if (!(0 <= i && i <= 14 && 0 <= j && j <= 14))
		{
			continue;
		}
		if (arr[i][j] == value)
		{
			count++;
			if (count > max)
			{
				max = count;
				if (max == 5)
				{
					return max;
				}
			}
		}
		else
		{
			count = 0;
		}
	}

	count = 0;

	for (k = -4; k <= 4; k++)
	{
		i = x - k;
		j = y + k;
		if (!(0 <= i && i <= 14 && 0 <= j && j <= 14))
		{
			continue;
		}
		if (arr[i][j] == value)
		{
			count++;
			if (count > max)
			{
				max = count;
				if (max == 5)
				{
					return max;
				}
			}
		}
		else
		{
			count = 0;
		}
	}

	return max;
}
